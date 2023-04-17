'''
BTK Akademi- Git ve Github: Versiyon Kontrolü
by Atıl Samancıoğlu

----------------------------------------

commit: kayıt noktaları, checkpointler yaratmak için komut
branch: dal, projenin bir noktadan birden fazla alana ayrılma noktası
repository,repo: git ver. kontrolünü içeren genel proje


                $git add                $git commit
çalışma klasörü --------> index-staging -----------> local repository
                   -proje arafta commit edilmedi-

----------------------------------------

$git status: git'in durumunu gösterir
$git init: git initilize, git'i bu klasör için başlat
*bir kere init çalıştırılmışsa daha çalıştırma, hata verebiliyor
*yanlışlıkla init çalıştırırsan ".git" klasörünü sil

-----------------------------------------


$git add x.py: untracked dosyaları git sistemine koymak için
$git commit -m "newFile.py was created": Add ile eklenmiş dosyaları mesajla birlikte commit eder
*mesaj zorunlu, şirketlerde genelde ingilizce ve standarda tabi.


$git log: logları gösterir
*hangi branch'e hangi commit edilmiş gösterir, commit'lere hash atar. Bu hash'le daha sonra o commit'e dönülebilir.
*author, date gösterilir


$git add . : her şeyi sisteme ekler


gitignore: seçtiğimiz dosyaların stage'e veya repo'ya eklenmesini engellemek için
*git status'de takip edilmesini de engelliyor, değişiklik yapsan da status'de gözükmüyor
*ayrıca git kaydetmediği için bu dosyanın sorumluluğu tamamen sende
.gitignore adlı bir dosya oluştur, klasör ya da dosya isimlerini buraya yaz

*gitignore template diye aratıp çalıştığın dil için hazır gitignore dosyaları bulabilirsin



'''
print("g4")