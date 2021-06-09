import sys
from .models import *
from rest_framework.decorators import api_view, permission_classes

from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
import random


class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    def parent(self, pos):

        return pos // 2

    def leftChild(self, pos):

        return 2 * pos

    def rightChild(self, pos):

        return (2 * pos) + 1

    def isLeaf(self, pos):

        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):

        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
                                            self.Heap[fpos])

    def maxHeapify(self, pos):

        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                if (self.Heap[self.leftChild(pos)] >
                        self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    def insert(self, element):

        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] >
               self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def Print(self):

        result = []
        for i in range(1, (self.size // 2) + 1):
            result.append(" PARENT : " + str(self.Heap[i]) +
                          " LEFT CHILD : " + str(self.Heap[2 * i]) +
                          " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

        return result

    def extractMax(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)

        return popped


@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def create_users(request, pk=None):

    for i in range(3):

        num = random.randint(0, 22000)
        username = 'username_'+str(num)
        first_name = 'first_name_'+str(num)
        email = 'email_'+str(num)+"@gmail.com"

        password = 'P@55word'+str(num)

        address = 'address_'+str(num)
        feedback = 'feedback_'+str(num)

        try:
            Users.objects.get(username=username)
        except Users.DoesNotExist:
            user = Users.objects.create_user(username=username, first_name=first_name,
                                             email=email, password=password)

            address_object = UserAddress.objects.create(
                address=address, user=user)
            feedback_object = UserFeedback.objects.create(
                feedback=feedback, user=user)

        except Exception:
            continue

    return Response({"status": "ok"}, 200)


@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def heapify_users(request, pk=None):
    user_list = Users.objects.filter(is_active=True)
    user_count = user_list.count()

    maxHeap = MaxHeap(user_count)
    for user in user_list:
        maxHeap.insert(user.id)

    result = maxHeap.Print()

    return Response(result, 200)
