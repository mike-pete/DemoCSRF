Simple-CSRF-GET-Demo

This is a simple web server that is useful for demoing the power of CSRF attacks.

To Use:
1. Run the server.py file.
2. Open a web browser and navigate to http://127.0.0.1:8080/bank<br>
   -This is a pretend bank page that lets you transfer money out of your account<br>
   -You start with $100 and lose money each time you make a transfer<br>

3. Now open a new tab and navigate to http://127.0.0.1:8080/cats<br>
   -This page has a hidden image on it.<br>
   -The image's src allows the attacker to automatically make a GET request as you. <br>
   -When your browser tries to load the image, money is automatically sent to the attacker.<br>

4. Reload the bank page, you are now missing $100!
