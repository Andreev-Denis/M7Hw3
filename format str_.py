team1 = 'Кодиры'
team2 = 'Декодеры'
team1_num = 6
team2_num = 7
score_1 = 20
score_2 = 23
team1_time = 10
team2_time = 10
tasks_total = score_2+score_1
time_avg = (score_2+score_1)/((team1_time*60)  + (team2_time*60))
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды:'+ team1
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды:' + team2
else:
    challenge_result = 'Ничья'
print('В команде %s участников: %d'% (team1, team1_num ))
print('В команде %s участников: %d'% (team2,  team2_num))
print('Итого сегодня в командах участников: %d и %d!'%(team1_num, team2_num))
print('Команда {} решила задач:{}'.format(team1, score_1))
print('Команда {} решила задач:{}'.format(team2, score_2))
print('{} решили задачи за:{} минут'.format(team1, team1_time))
print('{} решили задачи за:{} минут'.format(team2, team2_time))
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задачи. Среднее время решения задачи: {time_avg:10f} в секунду')