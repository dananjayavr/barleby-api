# Bartleby API 

### To run as a flask app
`env FLASK_APP=app.py flask run`

### Following scrapers are working:

Forty Thousand Quotations:
Prose and Poetical Choice Extracts on History, Science, Philosophy, Religion, Literature, etc.
Selected from the Standard Authors of Ancient and Modern Times<br>
Index: https://www.bartleby.com/348/index1.html

Dictionary of Quotations
From Ancient and Modern, English and Foreign Sources
Including Phrases, Mottoes, Maxims, Proverbs, Definitions, Aphorisms, and Sayings of Wise Men,
in Their Bearing on Life, Literature, Speculation, Science, Art, Religion, and Morals,
Especially in the Modern Aspects of Them<br>
Index: https://www.bartleby.com/345/index1.html

Familiar Quotations with Parallel Passages from Various Writers<br>
Index : https://www.bartleby.com/77/index1.html ... https://www.bartleby.com/77/index8.html

Hoyt’s New Cyclopedia of Practical Quotations
Drawn from the Speech and Literature of all Nations, Ancient and Modern, Classic and Popular,
in English and Foreign Text.<br>
Index: https://www.bartleby.com/78/index1.html

Prose Quotations from Socrates to Macaulay<br>
Index: https://www.bartleby.com/349/index1.html

Familiar Short Sayings of Great Men
With Historical and Explanatory Notes. (Note. formatting issues. ex. author bio repeated twice)<br> 
Index : https://www.bartleby.com/344/

Proverbs, Maxims and Phrases of All Ages<br>
Index: https://www.bartleby.com/89/index1.html

A Dictionary of Similes<br>
Index: https://www.bartleby.com/161/index1.html ... https://www.bartleby.com/161/index6.html

### Following does not seems to be working

John Bartlett, comp. (1820–1905).  Familiar Quotations, 10th ed.  1919.<br>
Index: https://www.bartleby.com/100/

Respectfully Quoted
A Dictionary of Quotations Requested from the Congressional Research Service<br>
Index : https://www.bartleby.com/73/index1.html

English Proverbs and Proverbial Phrases
Collected from the Most Authentic Sources
Alphabetically Arranged and Annotated with Much Matter Not Previously Published<br>
Index: https://www.bartleby.com/347/1.html ... https://www.bartleby.com/347/54.html

Curiosities in Proverbs
A Collection of Unusual Adages, Maxims, Aphorisms, Phrases and Other Popular Dicta from Many Lands
Classified and Arranged with Annotations<br>
Index: https://www.bartleby.com/346/

The Moral Maxims and Reflections of the Duke de la Rochefoucauld<br>
Index: https://www.bartleby.com/350/

The Characters of Jean de La Bruyère<br>
Index: https://www.bartleby.com/351/

Selections from the Characters, Reflexions and Maxims<br>
Index: https://www.bartleby.com/352/1.html

The Cynic’s Breviary<br>
Index: https://www.bartleby.com/353/1.html

Joseph Joubert A Selection from His Thoughts<br>
Index: https://www.bartleby.com/354/

A Thousand Flashes of French Wit, Wisdom, and Wickedness<br>
Index: https://www.bartleby.com/355/


### Todo : According to priority
 - Clean up JSON objects returned to remove empty strings, unicode character codes, etc.
 - Offer HTML interface to choose from quotation source, author, etc. (w/ API endpoint(s))
 - Containerize the application
 - Attempt to implement non-working scrapers
 - Add the quotations to a database 
 - Implement caching / https://realpython.com/caching-external-api-requests/