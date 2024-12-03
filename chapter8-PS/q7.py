# to remove a word from a list and strip it at the same time using function

# mera code logic jo mujhe khud nhi samajh aa raha
# list = ["Vaishnavi","Disney","Kdrama","Food","Winter","K-pop","Delusion","Reality"]
# def rem(list, word):
#     if(word not in list):
#         print("Invalid word")
#     for item in list:
#         list.remove(word)
#         return list
# word = input("Enter the word to be removed:")
# print(list, rem(word))

# harry bhai ka code logic 
def rem(list, word):
    n=[]
    for item in list:
        if not(item==word):
            n.append(item.strip(word))
    return n

list = ["Vaishnavi","Disney","Kdrama","Food","Winter","K-pop","Delusion","Reality"]
print(rem(list,"Reality"))