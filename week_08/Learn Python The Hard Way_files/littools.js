
function id_paragraphs() {
    $each($all('p'), function (p, i) {
         p.id = 'p' + i.toString();
    });

}

$boot(id_paragraphs);

/*
     FILE ARCHIVED ON 14:11:46 Aug 12, 2016 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 03:44:00 Feb 21, 2018.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/