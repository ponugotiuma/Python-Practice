# 1, Create an Empty list called shorts_list. add 5 video titles to it using append(),then print only first & last title using indexing.
'''lst=[]
lst.append("Room 404")
lst.append("Wrong Number")
lst.append("Blue Birthday")
lst.append("Hostel 2AM")
lst.append("Penthouse")
print(lst[::4])'''

# 2, You have a list of Views on YTShortsb, Write program to find & print how many shorts crossed 5000 views and print avg views.
'''yt_views=[1200,5400,890,15200,4500,2300,18100]
count=0
for views in yt_views:
    if views>5000:
        count+=1
print("views crossed 5000 :", count)
total_views=sum(yt_views)
numof_videos=len(yt_views)
avg_views=total_views/numof_videos
print("avg views are: ", round(avg_views,2))'''

# 3, You have a list of sub-parts names of short film ,
## a, change "part-2:love" to "part-2:library love"
## b, insert a new part "part 1.5 : the key" at index 1.
## c,print the updated list.
'''stories=["Part 1: Diary","Part 2: Love","Part 3: Girl Missing"]
stories[1]="Part 2: Library Love"
stories.insert(1,"Part 1.5 : The Key")
print(stories)'''

# 4, removing os corrupted clips from the raw footage list.
## a, remove all occurances of "corrupt.mp4" using a loop.
## b, delete the last clip using pop() and print which clip was removed.
## c, print the final list.
'''clips=["intro.mp4","corrupt.mp4","scene1.mp4","corrupt.mp4","outro.mp4"]
while "corrupt.mp4" in clips:
    clips.remove("corrupt.mp4")

removed_clip=clips.pop()
print(f"Removed clip was : {removed_clip}")
print(clips)'''

# 5, hostel Expenses
## a, Print total amount of 5days in the list.
## b, print the max/highest amount in the expenses.
## c, print a new list for the expenses less than 100 (<100).
expenses=[120,80,250,40,300]
total_amount=sum(expenses)
print("Total amount:", total_amount)
highest_amount=max(expenses)
print("The highest amount is :", highest_amount)
small=[]
for price in expenses:
    if price<100:
        small.append(price)
print(small)
