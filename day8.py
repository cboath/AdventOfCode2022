# trees = open('treeheight.txt', "r")
# sizedUp = trees.read().split('\n')

# border = (len(sizedUp) * 2) + (len(sizedUp) * 2 - 4)

# print(border)

# colCounter = 0
# rowCounter = 0
# indexOfGreatestVert = 0
# indexOfGreatestHor = 0

# # def isRowBigger(current, new):
# #     print('hi')

# # def isColBigger(current, new):
# #     for n in range(len(sizedUp)):
# #         if 

# for y in range(len(sizedUp)):
#     currentVisHt = 0
#     currentColHt = 0
#     for x in range (len(sizedUp[y])):
#         lessType = int(sizedUp[y][x])
#         # print('less: ', lessType)
#         if(currentVisHt < lessType):
#             currentVisHt = lessType
#             rowCounter += 1
#         for z in range(x):
#             moreType = int(sizedUp[z][y])
#             # print('CurColHt: ', currentColHt)
#             # print('CurVidlHt: ', currentVisHt)
#             # print('more: ', moreType, x, z, y)
#             # print('--------------------------------')
#             if(currentColHt < moreType):
#                 currentColHt = moreType
#                 colCounter += 1
#         # print(colCounter)
#         # print('***********************************************************')

# for y in range(len(sizedUp), 0, -1):
#     print('blue', y)
#     currentVisHt = 0
#     currentColHt = 0
#     y=y-1
#     for x in range(len(sizedUp[y]), 0, -1):
#         x=x-1
#         print('red', x)
#         lessType = int(sizedUp[y][x])
#         # print('less: ', lessType)
#         if(currentVisHt < lessType):
#             currentVisHt = lessType
#             rowCounter += 1
#         for z in range(x, 0, -1):
#             z=z-1
#             print('yel;low')
#             moreType = int(sizedUp[z][y])
#             # print('CurColHt: ', currentColHt)
#             # print('CurVidlHt: ', currentVisHt)
#             # print('more: ', moreType, x, z, y)
#             # print('--------------------------------')
#             if(currentColHt < moreType):
#                 currentColHt = moreType
#                 colCounter += 1
#         print(colCounter)
#         # print('***********************************************************')

# print(rowCounter + colCounter - 99 - border)



# # 1970 too high


d=[x.strip()for x in open('treeheight.txt').readlines()]
r,v=99+98+98+97,0
m=[(-1,0),(1,0),(0,-1),(0,1)]
for p in [0,1]:
 for i in range(1,len(d)-1):
  for j in range(1,len(d)-1):
   s=1
   for k in m:
    c,x,y=0,i+k[0],j+k[1]
    while 0<x<len(d)-1>y>0 and d[i][j]>d[x][y]and p==0:x,y=x+k[0],y+k[1]
    if d[i][j]>d[x][y]and(x==0 or x==len(d)-1 or y==0 or y==len(d)-1)and p==0:r+=1;break
    while 0<=x<=len(d)-1>=y>=0<p:
     c+=1
     if d[i][j]<=d[x][y]:break
     x,y=x+k[0],y+k[1]
    s*=c
   v=max(v,s)
print(r,v)