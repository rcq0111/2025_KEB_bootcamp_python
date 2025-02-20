
class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


def delete(deleteName, root):
    current = root
    parent = None
    while True:
        if deleteName == current.data:
            if current.left is None and current.right is None:
                if parent.left == current:
                    parent.left = None
                    print(f"{deleteName}이(가) 삭제 되었습니다.")
                else:
                    parent.right = None
                    print(f"{deleteName}이(가) 삭제 되었습니다.")
                del (current)
            elif current.left is not None and current.right is None:
                if parent.left == current:
                    parent.left = current.left
                    print(f"{deleteName}이(가) 삭제 되었습니다.")
                else:
                    parent.right = current.left
                    print(f"{deleteName}이(가) 삭제 되었습니다.")
            elif current.left is None and current.right is not None:
                if parent.left == current:
                    parent.left = current.right
                    print(f"{deleteName}이(가) 삭제 되었습니다.")
                else:
                    parent.right = current.right
                    print(f"{deleteName}이(가) 삭제 되었습니다.")
            else:  # 자식이 두 개 있는 경우
                current.data = search_delete_node(current, current.right)
                print(f"{deleteName}이(가) 삭제 되었습니다.")
            break
        elif deleteName < current.data:
            if current.left is None:
                print(f"{deleteName}이(가) 트리에 없음")
                break
            parent = current
            current = current.left
        else:
            if current.right is None:
                print(f"{deleteName}이(가) 트리에 없음")
                break
            parent = current
            current = current.right


def search_delete_node(parent, current):
    if current.left is None:
        data = current.data
        delete(current.data, parent)
        return data
    else:
        return search_delete_node(current, current.left)


if __name__ == "__main__":
    groups = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']
    #groups = [10, 15 ,8, 3, 9]
    root = None

    node = TreeNode()
    node.data = groups[0]
    root = node

    for group in groups[1:]:
        node = TreeNode()
        node.data = group
        current = root

        while True:
            if group < current.data:
                if current.left == None:
                    current.left = node
                    break
                current = current.left # move
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right # move


    print("BST 구성 완료")

    parent = None
    current = root
    deleteName = input()

    delete(deleteName, root)


    find_group = input()

    current = root
    while True:
        if find_group == current.data:
            print(f"{find_group}을(를) 찾았습니다.")
            break
        elif find_group < current.data:
            if current.left is None:
                print(f"{find_group}이(가) 존재하지 않습니다.")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_group}이(가) 존재하지 않습니다.")
                break
            current = current.right
