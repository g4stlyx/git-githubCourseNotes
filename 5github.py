'''
BTK Akademi- Git ve Github: Versiyon Kontrolü
by Atıl Samancıoğlu

Github
----------------------------------------
github: projelerin depolanabildiği, git komutlarını ve fonksiyonlarını kullanmaya 
olanak sağlayan, insanların birlikte daha rahat ve efektif bir şekilde çalışmasına 
yarayan bir portal.

en çok bu kullanılıyor, daha az kullanılsa da alternatiflerinden biri gitlab

contributions: commit yapmak, issue açmak(projede bir sorun var help), pull request yapmak

star: daha sonra bakmak için kaydetmek
fork: 
issues: hataları göstermek, sorun varsa sormak için (in a project)
pull request: -pr- senin olmayan bir projeye commit isteği atmak

------------ Github'a repo eklemek ------------------------

$git remote add origin https://github.com/g4stlyx/githubCourse.git
*origin: linki origin olarak kaydeder, her zaman link eklemek zorunda kalmayız

$git push -u origin master
*sign in ekranı çıkar, giriş yaparsın, bir daha girişe ihtiyacın kalmaz
-u: upstream: push yapılınca origin linkine ve master branch'ine git 
default olarak kaydeder. 
bu komut bir kere çalıştırıldıktan sonra $git push direkt push eder.

eg: $git push origin branch_name

------------ Compare & Pull Request ------------------------
(on github)
commit öncesini ve sonrasını kıyaslar, daha sonra 
"proje sahibine iki branch'i birleştir" isteği oluşturur.

------------ Fetch & Pull ----------------------------------
github ile local projeyi senkronize etmek için
(on local -git terminal-)

$git branch -r: remote(github'daki) branch'leri görmek için
$git checkout origin/master: remote branch'ler için switch komutu
*git switch origin/master çalışmaz, çünkü origin/master local değil remote branch

$git fetch origin master: origin adlı linkten master branch'ini local'e getir  
daha güvenli, local repoya değişiklikleri getiriyor ama dosyaları değişmiyor
dosyaları değişmeden önce analiz için imkan sağlıyor

$git pull origin master: git fetch + git merge 
direkt github'dan değişiklikleri getirip yeni commitle merge eder.

------------ Clone  --------------------------------

1)on terminal > $git clone https://github.com/g4stlyx/qweqwe
dosyaları indirmek için

2)on github >> fork >> projeyi kendi hesabına kopyalamak için
*aynı projeyi aynı adla kendi hesabında repo oluşturmak için

----------- Pull Request -------------------------------

x kişisinin projesinde değişiklik yapıp ona bu değişikliği projeye ekleme isteği atmak

x kişisinin seçenekleri:

1)not yazarak yapılan değişikliğin biraz değişitirilmesini isteyebilir.

2)approve edip değişiklik proje ile merge edilebilir.

3)close pull request ile direkt reddedebilir.


-------------- Private Repo'lar --------------------------
sadece özel izin verilen kullanıcıların görebildiği ve push edebildiği repo'lar.

settings >> collaborators >> manage access >> add


-------------- Diğer özellikler ---------------------------

actions: devops işlemleri için deployment/container kısımlar
projects: proje yönetimi aracı

README.md >> mark down >> html tarzı bir işaretleme dili >>
github md cheat sheet ile README dosyalarını daha estetik oluşturabilirsin.
ezberleme, netten bakarak yaz, html de içeride kullanılabiliyor.









'''
print("g4")