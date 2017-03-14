'''
Created on Feb 9, 2017

@author: Shani
'''
import bs4 as bs
import urllib.request

############################################### Getting the source code ##########################################

sourceUrl='https://www.pakwheels.com/forums/c/travel-n-tours'
sourceUrl2='https://www.pakwheels.com/forums/c/travel-n-tours/ask-travel-gurus'
sourceUrl3='https://www.pakwheels.com/forums/c/travel-n-tours/road-trips-vacations-hiking-trekking'
mainSource=urllib.request.urlopen(sourceUrl).read()
soup=bs.BeautifulSoup(mainSource,'lxml')
body=soup.body

mainSource2=urllib.request.urlopen(sourceUrl2).read()
soup2=bs.BeautifulSoup(mainSource2,'lxml')
body=soup2.body

mainSource3=urllib.request.urlopen(sourceUrl3).read()
soup3=bs.BeautifulSoup(mainSource3,'lxml')
body=soup3.body

blogUrls=[]

############################################### Finding all the links ############################################

# for url in soup.find_all('a'):
#     baseUrl='https://www.pakwheels.com'   
#     
#     # Filtering links  
#     
#     if((url.get('href').find('/forums/t/')!=-1) and (url.get('href').find('about-the-travel-n-tours-category')==-1) and (url.get('href').find('/forums/t/topic/')==-1)):
#         baseUrl+=url.get('href')
#         if(blogUrls.__contains__(baseUrl).__eq__(False)):
# #             print(baseUrl)
#             blogUrls.append(baseUrl)
#             
#             
# for url in soup2.find_all('a'):
#     baseUrl='https://www.pakwheels.com'   
#     
#     # Filtering links  
#     
#     if((url.get('href').find('/forums/t/')!=-1) and (url.get('href').find('about-the-travel-n-tours-category')==-1) and (url.get('href').find('/forums/t/topic/')==-1)):
#         baseUrl+=url.get('href')
#         if(blogUrls.__contains__(baseUrl).__eq__(False)):
# #             print(baseUrl)
#             blogUrls.append(baseUrl)


for url in soup3.find_all('a'):
    baseUrl='https://www.pakwheels.com'   
    
    # Filtering links  
    
    if((url.get('href').find('/forums/t/')!=-1) and (url.get('href').find('about-the-travel-n-tours-category')==-1) and (url.get('href').find('/forums/t/topic/')==-1)):
        baseUrl+=url.get('href')
        if(blogUrls.__contains__(baseUrl).__eq__(False)):
#             print(baseUrl)
            blogUrls.append(baseUrl)            
        
        
############################################### Getting all the text ############################################   
for url in blogUrls:
    print(url)
# for blogUrl in blogUrls:
#     print(blogUrl)
#     blogSource=urllib.request.urlopen(blogUrl).read()
#     blog=bs.BeautifulSoup(blogSource,'lxml')
#     body=blog.body
#     for paragraph in body.find_all('p'):
#         print(paragraph.text)
#     break
    
    
############################################# Getting Suggested Topics #########################################    
# testUrl='https://www.pakwheels.com/forums/t/i-want-to-go-gilgit-hunza-khunjrab-pass-need-expert-plan/465095/9'    
# source2=urllib.request.urlopen(testUrl).read()
# soup2=bs.BeautifulSoup(source2,'lxml')
# body2=soup2.body
# myDives = soup2.find_all('div')
# for div in myDives:
#     print(str(div.content()))
#     break
          
        
        


# for para in soup2.find_all('p'):
#     print(para.text)


    