# 포인터로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    """연결 리스트용 노드 클래스"""

    def __init__(self, data: Any = None, next: Node = None):
        """초기화"""
        self.data = data # 데이터
        self.next = next # 뒤쪽 노드 포인터

class LinkedList:
    """연결 리스트 클래스"""
    
    def __init__(self) -> None:
        """초기화"""
        self.no = 0         # 노드의 개수
        self.head = None    # 머리 노드
        self.current = None # 주목 노드

    def __len__(self) -> int:
        """연결 리스트의 노드 개수를 반환"""
        return self.no

    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는지 확인"""
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를 삽입"""
        ptr = self.head # 삽입하기 전의 머리노드
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data: Any):
        """맨 끝에 노드를 삽입"""
        if self.head is None:       # 리스트가 비어 있으면
            self.add_first(data)    # 맨 앞에 노드를 삽입
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1
    
    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head is not None:   # 리스트가 비어 있으면
            self.head = self.current = self.head.next
        self.no -= 1
    
    def remove_last(self):
        """꼬리 노드를 삭제"""
        if self.head is not None:
            if self.head.next is None:  # 노드가 1개 뿐이라면
                self.remove_first()     # 머리 노드를 삭제
            else:
                ptr = self.head     # 스캔 중인 노드
                pre = self.head     # 스캔 중인 노드의 앞쪽 노드

                while ptr. next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None         # pre는 삭제 뒤 꼬리 노드
                self.current = pre
                self.no -= 1

    def remove(self, p: Node) -> None:
        """노드 p를 삭제"""
        if self.head is not None:
            if p is self.head:          # p가 머리 노드이면
                self.remove_first()     # 머리 노드를 삭제
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return  # ptr은 리스트에 존재하지 않음
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)

    def clear(self) -> None:
        """전체 노드를 삭제"""
        while self.head is not None:    # 전체가 비어 있을 때까지
            self.remove_first()         # 머리 노드를 삭제
        self.current = None
        self.no
    
    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 이동"""
        if self.current is None or self.current.next is None:
            return False        # 이동할 수 없음
        self.current = self.current.next
        return True