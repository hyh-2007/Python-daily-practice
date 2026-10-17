"""Day1：Python 列表循环练习参考代码。

三道题均手写循环，不使用 max()、set() 或 index()。
这份代码是根据 day.md 的题目补充的参考实现。
"""


def reverse_list(values):
    """返回倒序的新列表，不改变原列表。"""
    result = []
    for i in range(len(values) - 1, -1, -1):
        result.append(values[i])
    return result


def find_max_and_first_index(values):
    """返回最大值和它第一次出现的下标；空列表会报错。"""
    if not values:
        raise ValueError("空列表没有最大值")

    largest = values[0]
    first_index = 0
    for i in range(1, len(values)):
        # 必须严格大于才更新；相等时保留第一次出现的下标。
        if values[i] > largest:
            largest = values[i]
            first_index = i
    return largest, first_index


def remove_duplicates(values):
    """删除重复元素，并保持元素第一次出现的顺序。"""
    result = []
    for value in values:
        if value not in result:
            result.append(value)
    return result


def main():
    values = [3, 1, 5, 2, 5, 3]
    print("原列表：", values)
    print("逆序结果：", reverse_list(values))
    largest, first_index = find_max_and_first_index(values)
    print("最大值：", largest)
    print("最大值第一次出现的下标：", first_index)
    print("去重结果：", remove_duplicates(values))


if __name__ == "__main__":
    main()
