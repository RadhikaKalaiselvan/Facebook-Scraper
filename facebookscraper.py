import facebook
import json

# __author__ == "Radhika Kalaiselvan"

if __name__ =='__main__':
    #basic attributes declaration
    token='YOUR FACEBOOK TOKEN'
    page='Expedia'
    max_count=8
    outputFile="Expedia_Page_Top_"+str(max_count)+"_Posts.txt"
    
    #Call to facebook graph API
    graph=facebook.GraphAPI(token)
    
    #List of fields to be fetched and their path in response
    field_names=['id',
            'message',
            'created_time',
            'shares',
            'likes.data(0).summary(true)',
            'comments.data(0).summary(true)',
            'reactions.type(LOVE).limit(0).summary(total_count).as(reactions_love)',
            'reactions.type(WOW).limit(0).summary(total_count).as(reactions_wow)',
            'reactions.type(LIKE).limit(0).summary(total_count).as(reactions_like)',
            'reactions.type(SAD).limit(0).summary(total_count).as(reactions_sad)',
            'reactions.type(ANGRY).limit(0).summary(total_count).as(reactions_angry)',
            'reactions.type(HAHA).limit(0).summary(total_count).as(reactions_haha)'
            ]
    
    #Generating the query
    fields_names=','.join(field_names)
    posts=graph.get_connections(page,'posts',fields=fields_names)
    
    #initialise the count
    count=0
    id_=[]
    message=[]
    created_time=[]
    
    likes_=[]
    comments_=[]
    positive_resp=[]
    negative_resp=[]
    all_response=[]
    shares_=[]
    
    print("Scrapping posts from ",page," page....")
    
    #Start scrapping..
    while count<max_count:
        try:
                for post in posts['data']:
                    if count>=max_count:
                        break
                    n_likes=post['likes']['summary']['total_count']
                    n_comments=post['comments']['summary']['total_count']
                    
                    #replacing \t in message since our final output contains column values which are \t separated. Can be easily load and used for further processing.
                    message.append(post['message'].replace('\t', ' '))
                    
                    #Catagorizing posts as positive and negative from the reactions data in FB
                    p_resp=post['reactions_love']['summary']['total_count']+post['reactions_wow']['summary']['total_count']
                    n_resp=post['reactions_angry']['summary']['total_count']+post['reactions_sad']['summary']['total_count']
                    positive_resp.append(p_resp)
                    negative_resp.append(n_resp)
                    likes_.append(n_likes)
                    comments_.append(n_comments)
                    id_.append(post['id'])
                    created_time.append(post['created_time'])
                    try:
                        #might throw an error if there are no shares
                        n_shares=post['shares']['count']
                    except KeyError:
                        n_shares=0
                    
                    #'all_response' is count of shares,likes,comments,positive response,negative response for a post. 
                    all_response.append(n_shares+n_comments+n_likes+p_resp+n_resp+post['reactions_haha']['summary']['total_count'])
                    shares_.append(n_shares)
                    count+=1
               
        except KeyError:
            break 
        
    top_posts = [{"ID": id_, "CREATED_TIME": time,"LIKES":likes_,"COMMENTS_COUNT":comments, "SHARES_COUNT":shares,"POSITIVE_RESPONSE":positive,"NEGATIVE_RESPONSE":negative,"ALL_RESPONSES_COUNT":all_count,"MESSAGE":messg} for  id_,time,likes_,comments,shares,positive,negative,all_count,messg in zip(id_,created_time,likes_,comments_,shares_,positive_resp,negative_resp,all_response,message)]
    with open(outputFile, 'w') as outfile:
        outfile.write(json.dumps(top_posts))         
    print("Completed Successfully. Kindly open ",outputFile," to check the output"
