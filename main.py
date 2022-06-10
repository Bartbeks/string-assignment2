# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_van_basten= 'Marco van Basten'
player_gullit= 'Ruud Gullit'
goal_0=32
goal_1=54

scorers = player_gullit +" "+str(goal_0)+","+" "+player_van_basten+" "+str(goal_1) 

# report = f'{player_gullit} scored in the {str(goal_0)}nd minute {player_van_basten} scored in the {str(goal_1)}th minute'
report = f'{player_gullit} scored in the {goal_0}nd minute\n{player_van_basten} scored in the {goal_1}th minute'

# Choose a player that played in the soccer match and store his name as a string in the variable player.
player ='Jan Wouters'
spaceloc=player.find(" ")

first_name = player[0:spaceloc]
last_name =player[spaceloc+1:len(player)]
last_name_len = len(last_name)


print(last_name)
name_short= f'{first_name[0:1]}. {last_name}'
x= len(first_name)

chant= f'{first_name}! '*x  
checkspace=chant[0:len(chant)-1]!=' '
chant=chant[0:len(chant)-1]

good_chant =chant[0:len(chant)-1]!=' '
print(good_chant)


       

