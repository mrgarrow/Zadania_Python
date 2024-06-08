# Zadanie 1

num_of_users = 9045
num_of_posts = 54822
num_of_likes = 251561

avg_posts_per_user = num_of_posts/num_of_users
print(round(avg_posts_per_user,2))
avg_likes_per_post = num_of_likes/num_of_posts
print(round(avg_likes_per_post,2))

# Zadanie 2

courses = {
'Introduction to Python',
'Web Development',
'Data Science',
'Artificial Intelligence'
}
query = 'Big Data'
for value in courses:
    if query not in courses:
        print(f'{query} course not found')
    else:
        print(f'{query} course found')
    break

# Zadanie 3

energy_output = [ 
[0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4],
[0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5],
[0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
]
out = 0
out_2 = 0
sum = 0
for value in energy_output:
    out = 0
    for i in value:
        out_2 += i
        out += i
    sum += out
print('Energia wygenerowana przez panele w ciągu dnia wynosi:',sum,'kWh')
