# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    # queries=[]
    # with open("trial.txt","r") as f:
    #     n = int(f.readline())
    #     queries=[f.readline().split() for i in range(n)]
    # return [Query(x) for x in queries] 
    # print(n,queries)  
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    # changed to an array with None if contact dosen't exists and the query at place if it exits.
    contacts = [None]*10**7
    
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            if contacts[cur_query.number]:
                contacts[cur_query.number].name=cur_query.name
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         contact.name = cur_query.name
            #         break
            else: # otherwise, just add it
                contacts[cur_query.number]=cur_query
                # contacts.append(cur_query)
        elif cur_query.type == 'del':
            if contacts[cur_query.number]:
                contacts[cur_query.number]=None
            # for j in range(len(contacts)):
            #     if contacts[j].number == cur_query.number:
            #         contacts.pop(j)
            #         break
        else:
            response = 'not found'
            if contacts[cur_query.number]:
                response=contacts[cur_query.number].name
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         response = contact.name
            #         break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

