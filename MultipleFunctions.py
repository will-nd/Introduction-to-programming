#Create alien name based on actor name

def create_actor(): #define create_actor function
    empty_list = [] #empty list to be filled
    return (empty_list) #returns empty_list when create_actor is called
#------------------------------------------------------------------------
def fillTheList(empty_list):
    empty_list = ["andrei stephens",
                  "harry venables",
                  "phillipa blythe",
                  "yuan spield",
                  "sadiq elbahi",
                  "stephanie wynne",
                  "zeng ergan"] #fill empty list
    full_list=empty_list
    return(full_list) 
#------------------------------------------------------------------------
def alien_name(full_list):
    alien_list = []

    for i in full_list:
        actor = i.find(' ')
        alien_list.append(i[actor+1:actor+4]+ i[1::-1])
    return(alien_list)
#------------------------------------------------------------------------
def actor_list(full_list):
    
    v_actor_list=full_list
    del v_actor_list[2] #deletes index 2 from v_actor_list
    del v_actor_list[4]
    return(v_actor_list)
#------------------------------------------------------------------------
def w_vowel(alien_list):
    vowels={"a","e","i","o","u"} #define list vowels
    voweless=[]
    vowel=[]

    for word in alien_list:
        if any(char in vowels for char in word): #if to remove none vowel alien names
            vowel.append(word)
        else:
            voweless.append(word)
    return(vowel)
#------------------------------------------------------------------------
def wo_vowel(alien_list):
    vowels={"a","e","i","o","u"}
    voweless=[]
    vowel=[]

    for word in alien_list: #for loop
        if any(char in vowels for char in word):
            vowel.append(word)
        else:
            voweless.append(word)
    return(voweless)
#------------------------------------------------------------------------
def extract(vowel):
    director=""

    for name in vowel:
        join_chars = name[:3]
        director = director+join_chars
    return(director)
#------------------------------------------------------------------------
def main():
    empty_list=create_actor()
    

    full_list=fillTheList(empty_list)


    alien_list = alien_name(full_list)

    v_actor_list = actor_list(full_list)

    vowel = w_vowel(alien_list)

    voweless = wo_vowel(alien_list)

    director = extract(vowel)
    print(director,"presents: Harry of the Rings")
    print("Actor-List                   \t Alien-List")
    print("----------                   \t ----------")
    for actor,alien in zip(v_actor_list,vowel):
        print(actor,"             \t",alien)
    print("-------------------------------------------")
    print("Possible usable alien names:")
    for name in voweless:
        print(name+"a")
    

main()
