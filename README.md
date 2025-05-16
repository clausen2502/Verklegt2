# Hopur18Verklegt2
# Castle Apartments

# Vefsíðan var launched á netið og notað azure blob container til þess að geyma myndirnar.
# Einnig settum við upp custom domain, en vorum í DNS veseni þar sem það var of lengi að updateast.
# Custom domainið virkaði ekki á HR netinu hjá okkur né ef við vorum á hotspot hjá NOVA, en virkaði
# á öðrum stöðum. Þess vegna í myndbandinu er custom domainið ekki alltaf notað. Við skilum kóðanum til að keyra
# kóðann á local domain, en custom og normal domain er launchað á öðru branchi á github sem er bara með öðruvísi
# settings.py og stillingar til þess að launcha serverinn.
# Custom domainið ætti að virka við yfirfærslu verkefnisins. 
# NORMAL-DOMAIN: 'castleapartments-etdbguf9gsfnafft.canadacentral-01.azurewebsites.net'
# CUSTOM-DOMAIN: 'castleapartments.space'

#Notkun
Notendur + password aðganga sem til eru: 
Seller - username: orrihrafn psw: 6636190iP
Admin - username: manager psw: 6636190iP
Buyer (ekki búinn að skrá sig sem seller) username: johannainga psw: 6636190iP
Einnig er einfalt að búa til aðgang frá grunni með 'Register'.
Seller/Real estate agency: username: lindfasteignasala psw: Fasteignir123

#Aukakröfur
Eftirfarandi eru aukakröfur verkefnisins:
"As a user/buyer I want to be able to sign in as a seller."
"As a buyer I want to be able to delete a offer that I created"
"As a seller, I want to create a new property listings with details and images."
"As a seller, I want to see my properties in the navigation bar."
"As a seller, I want to see the offers I have received in the navigation bar."
"As a seller, I want to put status on an offer I received (accepted, rejected or contingent)."
"As a user I want to read about the company in “about us” located in the footer."
"As a user I want to calculate a mortage in the “mortage calculator” in the footer."
"The system shall display a cookie notice on the user's first visit, informing them about the use of cookies, their purpose, and allowing the user to accept or reject them."
"As a guest, I want to browse available properties so I can explore options without registering."
"As a guest, I want to use filters (e.g. price, type, postal code) so I can narrow down the listings."
"As a guest, I want to be prompted to register if I try to submit a purchase offer."
"As an administrator, I want to view all users in the system."
"A navigation link labeled “Admin Dashboard” shall be visible only to authenticated admin users."
"The admin dashboard shall display a list of all registered users."
"The dashboard shall also display a list of all properties in the system."
"When the admin clicks delete on a user or property, the system shall: Prompt for confirmation."
"Admins shall be able to delete any user or property  by clicking a Delete button next to their entry."
"Each time a user clicks or views a property, the system shall increment a view count for that property."
"A section titled “Most Popular Properties” shall be displayed at in a designated area of the property catalogue page."
"The popularity list shall update dynamically based on view counts."
"A user with the seller role shall be able to  edit and delete only the properties they have personally submitted to the system."
"A user with the seller role shall be prompted with a modal saying "are you sure you want to delete this property?" "
"A user shall be able to delete a newly submitted offer that he just created."
"The system has officially launched, and the platform is live and publicly accessible."
"The system has a custom domain, which can be accessed by anyone."

#Cookies
Vefsíðan inniheldur cookies sem hægt er að samþykkja eða hafna. Ef cookies-glugginn kemur ekki upp á skjánum við notkun vefsíðunnar er hægt að setja eftirfarandi skipun í vafra-console (F12 → Console flipi) til að endurstilla valið: localStorage.removeItem('cookieConsent'); Þá mun glugginn birtast aftur næst þegar síðan er endurhlaðin.
