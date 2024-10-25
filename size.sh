#!/bin/bash
#Создаем процедуру определения размера
get_size() {
    local path="$1"
    local size=$(du -hs "$path" 2>/dev/null | cur -f1)
    echo $size
}
#помещаеи каталог контейнеров
items$(ls -A)

#Обнуляем резултат
result=()
#Запускае цикл для каждого элемента контейнера 

for item in $items; do
#определяем размер элемента вызовом процедуры и передачи элемента как параметра
    test=$(get_size "$item")
#Присваиваем результату результ
    result+=("$test $item")
done
#Выводим на экран результат с параметрами обратной сортирови
printf "%s\n" "${result[@]}" | sort - rh column -t