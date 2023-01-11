def test():
      da = ['sdhswgqwy','Сколько голов у человека?' , 'Сколько рук у человека? ','Скольков голов у Цербера?' , 'Сколько ног у кошки?', 'самый высший бал в школах Росии?']
      net = ['fsgdsg', 1, 2, 3, 4, 5]
      f = 0
      for i in range(5):
            d = int(input('напиши номер вопроса'))
            print(da[d])
            a = int(input('введи ответ'))
            if a != net[d]:
                  print('вы неправы!')

                  continue
            else:

                  print('молодец')
            f += 1
      print('vash result', f)
      if f == 1:
            print('вы супер плохо знаете материал')
      elif f == 2:
            print('вы не супер плохо знаете материал')
      elif f == 3:
            print('пойдет')
      elif f == 4:
            print('почти красава')
      else:
            print('ты кайфарик!!!!!')
test()
www = int(input('Напиши 1 если хочешь, пройти еще раз, 2 если нет'))
if www == 1:
      test()

else:
      print('Хорошего дня')