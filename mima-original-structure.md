# Original Website Structure: mima.co.il

## Pages
* Home page: https://www.mima.co.il/
* Search by name page: https://www.mima.co.il/artist_page.php?artist_id=xx
* Search by song page: https://www.mima.co.il/artist_letter.php?let=xx
* General search page: https://www.mima.co.il/search_result.php
* Fact page: https://www.mima.co.il/fact_page.php?song_id=xx
* Artist's songs page: https://www.mima.co.il/artist_page.php?artist_id=xx

## Entities and Relationships

### Artists
* id (auto_p_k - int)
* name (string)

### Songs
* id (auto_p_k)
* name (string)
* artist (art_id - int)

### Facts
* Author  (string)
* Song (song_id - int)