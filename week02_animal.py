animals = [{"name":"코끼리", "weight":6, "preference":6},
           {"name":"하마", "weight":4, "preference":3},
           {"name":"기린", "weight":5, "preference":5},
           {"name":"물소", "weight":3, "preference":4},
           {"name":"호랑이", "weight":2, "preference":1},
           {"name":"사자", "weight":2, "preference":1},
           {"name":"얼룩말", "weight":2, "preference":1},
           ]
#print(animals)
#animals.sort(key=lambda animal: animal["preference"]) #오름차순 by 선호도
animals.sort(key=lambda animal: animal["preference"], reverse=True) #내림차순 by 선호도
#print(animals)

loaded_animals = list() #트럭에 적재되는 동물들의 이름을 담을 리스트
current_weight = 0 #현재 트럭에 실은 동물들의 무게 합
total_preference = 0 #트럭에 태운 동물들의 총 선호도 합

for animal in animals:
    if current_weight + animal["weight"] <= 7:
        loaded_animals.append(animal["name"])
        current_weight += animal["weight"]
        total_preference += animal["preference"]

print(f"트럭에 탑승한 동물들 : {loaded_animals}\n총 중량 : {current_weight}톤\n총 선호도 : {total_preference}")

"""
책에 있는 코드 미리 다운받아두기
람다 공부하기
"""