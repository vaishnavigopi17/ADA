
def sort(arr):

 for i in range(0,len(arr)):
   min=i

   for j in range(i+1, len(arr)):
      if arr[j]<arr[min]:
         min=j
    
   arr[i],arr[min]=arr[min],arr[i]

 return arr

arr=[]
n=int(input("Enter the num. of elemts you want to enter:"))

for a in range(n):
  k=int(input("Enter the elemnts into an array:"))
  arr.append(k)

print("The sorted elements are:",sort(arr))
