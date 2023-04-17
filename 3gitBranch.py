'''
BTK Akademi- Git ve Github: Versiyon Kontrolü
by Atıl Samancıoğlu

----------------------------------------

Branch: Herhangi bir sebeple projeyi bir noktadan dallara ayırıp 
iki veya daha fazla koldan farklı şekillerde geliştirmek

master: ana branch'in default ismi; projenin ana, en eksiksiz hali
head: bulunduğumuz yer

git branch feat: feat(feature-özellik-) adında branch oluşturur
git merge feat: bulunduğumuz branch ile feat branch'ini birleştirir

git branch: var olan branch'leri gösterir
git switch feature: feature adlı branch'e geçiş yapar
*her branch'in dosyası ayrı tutuluyor, branch değişince
değişilen branch'in dosyaları yok olmuş gibi gözüküyor
*watch the video 3.2-git branch>merge- for visualizition
it's way more clear that way


********** 3.3 FAST FORWARDING

master üzerinden a branch'i açıp MASTER'DA DEĞİŞİKLİK YAPMADAN a'da 
değişiklik yaptıktan sonra a'yı master'la birleştirmek: 
fast forwarding -ileri sarma- *kursta görsellere bak daha net oturur
bu durumda commit mesajı bile istemez; çünkü iki branch'i birleştirmedi,
sadece a'da yapılan her şey master'ın içine eklendi

********** 3.4 MERGE CONFLICT -çakışma

master'da a.txt var içinde 123 yazıyor, 
b branch'i açıp a.txt'yi sildik başka bir txt oluşturduk.

b ile master'ı birleştirirken auto yapamıyor, conflict'leri çözmeni istiyor.
çözmek için silinen a'yı geri getir.

conflict aynı dosya içinde de olabilir:
txt.txt'de 123 yazıyor master'da commit ettim
a branch'ine girip txt.txt'yi 231241241 olarak değiştirdim(123 yok)
a ile master'ı merge ederken auto yapmıyor, soruyor:
123 mü olsun 231241241 mi? birini bırakıp ya da ikisinden farklı bir şey
yazılıp merge edilebilir

********** 3.5 STASH

a branch'inde commit yapmak istemediğimiz bir durumdayız, işimiz henüz bitmedi.
ama acil master'a gitmemiz gerekiyor:

***a'da master'da olmayan bir dosya düzenlenmişse/eklenmişse a'nın içeriği commit 
edilene kadar master'a getirilir.
a.txt var, commit etmedin ve çakışmıyor, a.txt commit edilene ya da branch 
değişene kadar master branch'inde kalır.

***a'da master'da olan bir dosyanın içeriğini değiştirdin:
ya hata verir, değişiklik commit etmeden branch değişmek istediğin için
ya da içeriği master'daki haline dönüştürür, onun dışındaki özellikleri master'a
getirir(saçma sapan bir durum)

"git restore a.txt" yaparak dosya master'daki haline getirilebilir
ancak a branch'indeki değişiklikler a'da da kaybolur.
bu istenmeyen bir durum çünkü a branch'inde yapılan commit edilmemiş
değişiklikler artık hiçbir yerde yok.


3 seçenek var:
*Commit etmek
*Değişikliklerden vazgeçmek
*Stash yapmak: (saklamak depolamak) commit edilmemiş değişiklikleri bir yerde
saklar. Bu değişiklikler ne çalışma klasöründe ne indexte ne repo'da olur,
stash diye ayrı bir yerde saklanır. İstediğimiz zaman geri getirebiliriz.

$git stash: commit etmek istemediğin değişiklikleri, branch'i terk etmek 
zorunda kaldığın bir durumda saklamak için kullanılır.

$git stash pop: sakladığım değişiklikleri uygulamak istediğim yerdeyim,
geri getirir.

****** ayrıntı ama mülakatlarda gelebilir

$git stash list: zuladığımız değişikliklerin listesi
$git stash apply stash@{0} : istediğim stash'i uygulatmak için

$git stash clear: zulayı siler
$git stash apply: son stash'i pop'un aksine listeden silmez, ama uygular.






'''
print("g4")