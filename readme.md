DFS Path: ['Vokzalna', 'Metrobudivnykiv', 'Metalurhiv', 'Zavodska', 'Prospekt Svobody', 'Pokrovska']
BFS Path: ['Vokzalna', 'Metrobudivnykiv', 'Metalurhiv', 'Zavodska', 'Prospekt Svobody', 'Pokrovska']

Різниця в шляхах:
DFS шлях: Vokzalna -> Metrobudivnykiv -> Metalurhiv -> Zavodska -> Prospekt Svobody -> Pokrovska    
BFS шлях: Vokzalna -> Metrobudivnykiv -> Metalurhiv -> Zavodska -> Prospekt Svobody -> Pokrovska   

Пояснення:
DFS (Depth-First Search):

DFS досліджує кожен шлях до кінця, перед тим як перейти до наступного сусіда.
Це може призвести до знаходження довшого шляху, якщо він першим досягне мети.
Перевага: Простота реалізації. Недоліки: Може знайти довші шляхи у деяких випадках.

BFS (Breadth-First Search):
BFS досліджує всі вузли на поточному рівні перед переходом до вузлів на наступному рівні.
Це гарантує знаходження найкоротшого шляху у ненавантаженому графі.
Перевага: Гарантія найкоротшого шляху. Недоліки: Може споживати більше пам'яті.
Ці алгоритми показують різні результати через свій порядок дослідження вузлів. BFS завжди знайде найкоротший шлях, тоді як DFS може знайти довший шлях залежно від порядку відвідування вузлів.