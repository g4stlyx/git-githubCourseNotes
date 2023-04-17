'''
BTK Akademi- Git ve Github: Versiyon Kontrolü
by Atıl Samancıoğlu

Git- Going Back
----------------------------------------

****commit yapmadın değşiklik yaptın ama geri dönmek istiyorsun: $git restore brokenFile.py

****commit yaptın ama değişiklikleri beğenmedin/bir şeyler bozuldu, geri dönmek istiyorsun:
1)$git checkout <hashOfCommitYouWantToGo>

*bunu yapınca "detached(kopuk) head" durumu oluyor: 
son commit artık head değil, bu bir sorun.
çözümü:

1.1)$git switch master: geldiğimiz-son- commit'e geri döndük;
head düzeldi ancak geri almak istediğimiz değişiklikler duruyor.

1.2) $git branch feat, $git switch feat, $git add ., $git commit
head düzeldi, yeni bir branch üzerinden geri dönmüş olduk.
eğer geri almak istediğimiz değişiklikleri görmek istiyorsak master branch'te duruyor.

2) $git reset <hashOfCommitYouWantToGo>: yapılan commitleri siler
detached head olmaz.

3) $git reset --hard <HashOfCommitYouWantToGo>: 
yapılan commitler+ o commitlerde yapılan değişiklikleri siler
detached head olmaz.
dikkatli kullanılması gerekiyor, yapılan değişiklikler silinince geri gelmiyor.

4) $git revert <HashOfCommitYouWantToGo>:
geri dönmek istenen yere yeni bir commit oluşturarak gider.
6'dasın 4'e dönmek istiyorsun: 7'yi 4'ün özellikleriyle oluşturur.
5 ve 6'yı silmez.


************************** $git diff

$git diff: git add yaptıktan sonra yapılan değişiklikleri gösterir.
$git diff HEAD: son commit'e göre ne değiştiğini gösterir
$git diff <hash1> <hash2>:hash1 hash2 commitleri arası farkı gösterir.
$git diff master feature: master ve feature branch'leri arasındaki farkı gösterir.


*************************** $git rebase

çok kullanılmaz, mülakatlarda çok sorulur

merge commit'lerden kurtulmak için yapılan boş bir eylem. kullanmaya gerek yok.
merge commit logları silinir, tarih yeniden yazılıp loglar düzene sokulur

2 branch var yan yana gidiyorlar ve çakışmıyorlar, rebase yapılırsa
master feat'in arkasına gelir, merge commitlerden kurtulunur ama tarih değişiyor.

*görselle çok daha iyi anlaşılıyor.*

asla kullanmaman gereken durum:
projeni başkalarıyla paylaşmışsan, başkalarında bu proje varsa.







'''
print("g4")