# preorder : PLR / postorder : LRP / inorder : LPR

# def pre_order(node):
#     if node is None:
#         return
#     print(node.data, end='-')
#     pre_order(node.left)
#     pre_order(node.right)
#
# def in_order(node):
#     if node is None:
#         return
#     in_order(node.left)
#     print(node.data, end='-')
#     in_order(node.right)
#
# def post_order(node):
#     if node is None:
#         return
#     post_order(node.left)
#     post_order(node.right)
#     print(node.data, end='-')

class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

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

    print("BST 구성 완료")

    parent = root

    deleteName = '마마무'
    #deleteName = input()

    while True:
        if deleteName == current.data:

            if current.left == None and current.right == None:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None

            elif current.left != None and current.right == None:
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left

            elif current.left == None and current.right != None:
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right

            #else:

        elif deleteName < current.data:
            if current.left == None:
                print(f"{deleteName}이(가) 트리에 없음")
                break
            parent = current
            current = current.left
        else:
            if current.right == None:
                print(f"{deleteName}이(가) 트리에 없음")
                break
            parent = current
            current = current.right


