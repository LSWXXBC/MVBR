import random
import numpy as np
from torch.utils.data.sampler import Sampler
import pdb
# import matplotlib.pyplot as plt

def huatu(number_type):
    y1 = number_type
    x1 = range(len(number_type))

    plt.plot(x1, y1)
    plt.xlabel('type')
    plt.ylabel('number')
    plt.title('distribution')
    plt.legend()
    plt.show()

def cls_sample(answers, index, labels):
    num_class = len(labels)
    num_ans = len(index)
    cls_data_list = [list() for _ in range(num_class)]
    print("cls_data_list length", len(cls_data_list))

    for j in range(0, len(labels)):
        for i in index:
            if labels[j] in answers[i]['labels']:
                cls_data_list[j].append(i)

    # label_num_min = min([len(x) for x in cls_data_list])
    # print("label nun min :", label_num_min)

    x = []
    while len(x) < 1000:
        for m in range(0, len(cls_data_list)):
            a = random.sample(cls_data_list[m], 1)
            x.append(a)
    # for n in range(0, int(num_ans/num_class)):
    #     for m in range(0, len(cls_data_list)):
    #         a = random.sample(cls_data_list[m], 1)
    #         x.append(*a)
    return x


def num_typ(answers):
    print("every type numbers function")
    q_type = []
    number_type = []
    for ans in answers:
        q_type.append(ans["question_type"])
    q_type = np.unique(q_type)
    type_num = len(q_type)
    print('type_num', type_num)

    for i in range(len(q_type)):
        m = 0
        for j in range(len(answers)):
            if answers[j]["question_type"] == q_type[i]:
                m += 1
        print(q_type[i], 'num', m)
        number_type.append(m)
    number_type.sort(reverse=True)
    print(number_type)

    return number_type


def class_re_sample_forward(answers):
    print("class_re_sample begin")

    q_type = []
    for ans in answers:
        q_type.append(ans["question_type"])
    q_type = np.unique(q_type)

    x = []
    balance_data_index = []
    for i in q_type:

        tem_ans_index = []
        # tem_ans = []
        labels = []

        for index_ans, temp in enumerate(answers):
            if i == temp['question_type']:
                tem_ans_index.append(index_ans)

        tem_ans = [answers[k] for k in tem_ans_index]
        for temp in tem_ans:
            if not temp['labels']:
                continue
            for k in range(0, len(temp['labels'])):
                labels.append(temp['labels'][k])
        # for temp in answers:  # temp: dict
        #     if i == temp["question_type"]:
        #         tem_ans.append(temp)
        #         for k in range(0, len(temp["labels"])):  # temp['labels'] : list
        #             if len(temp) == 0:
        #                 continue
        #             labels.append(temp["labels"][k])
        labels = np.unique(labels)

        print("q_type" + " " + i)
        print(len(tem_ans_index))
        new_answers_index = cls_sample(answers, tem_ans_index, labels)

        for k in new_answers_index:
            x.append(k)
    for q in range(0, len(x)):
        balance_data_index.append(*x[q])
    # print("match question begin")
    #
    # for i, m in enumerate(x):
    #     print("num:", i)
    #     for n in questions:
    #         if m['question_id'] == n['question_id']:
    #             y.append(n)
    balance_data_index = np.unique(balance_data_index)
    print(len(balance_data_index))
    print ("class_re_sample finish")
    return balance_data_index

def test_fun(data):

    x = 1
    for i in range(0, len(data)):
        if not data[i].has_key('question_id'):
            print('i find you', i)
            x = 2
    if x == 1:
        print('not find')
