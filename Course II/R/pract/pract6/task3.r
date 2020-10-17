'
Создать функцию, которая по переданному параметру возвращает
наименование дня недели на русском языке.
Если переданное число больше 7, делить на 7 и определять день недели по остатку от деления.
Если число меньше 1, функция возвращает пробел.
Если число действительное, округлять до целого.
'
#Функция
calc <- function(number, parameter = "rus") {
  #Округление
  number <- round(number, 0)
  
  #Если больше - берем остаток
  if (number > 7) {
    number <- number %% 7
  }
  #Если меньше 1 - пробел
  if (number < 1) {
    return(" ")
  }
  
  #Если есть английский - выводим на англе
  if (is.element(parameter,
                 c("Eng", "eng", "English", "english", "англ", "Англ", "анг"))) {
    day <- switch (
      number,
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    )
    #Если нет английского -выводим на русском
  } else{
    day <- switch (
      number,
      "Понедельник",
      "Вторник",
      "Среда",
      "Четверг",
      "Пятница",
      "Суббота",
      "Воскресенье"
    )
  }
  
  #Отдаем значение
  return(day)
}

#Основная программа
{
  #Запускаем функцию нормально
  result <- calc(20)
  print(result)
  
  result <- calc(20, "Eng")
  print(result)
}