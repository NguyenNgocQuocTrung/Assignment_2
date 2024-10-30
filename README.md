### Have a nice day Ms Hannah!

This is **README** file to explains how to set up the **environment** and run the **scripts**.

<h1 style="color:#fe9600;"> Prequisites: </h1>

 - Use **Python** for supporting Selenium
 - Set up IDE on **Visual studio code**
 - Install and configure Selenium Webdriver
 - Choose **Edge** for Browser, ensure the correct Webdriver
 - Manage project dependency by **Pip**
 - Use **Github** for version control system


<h1 style="color:#fe9600;"> Step to run code: </h1>

 - Create **Conftest.py** to set up **Edge** driver
    - I have two ways set up **Edge**: Specific **PATH** for Edge driver and Automatically find new version
    - When you use *the former*, it will *Edge* faster, but may be encounter the error not suitable version.
    - In contrast, when you use *the latter*, it won't encounter error but slower due to timing to download latest version
    - Please remember *import pytest* and *@pytest.mark.usefixtures("driver")* before you use each module!

 - Run each test case you want, but may be you will see **Cloudflare** force you to verify "Im a human". It will hidden your process testing when code is running. You can try to download **Opencart** in localhost to fix this error!
 - Maybe you can see some failed testcase, but it's not your fault, the reason is **OpenCart** has problem!
 - Code will create report.html if you run **pytest --html=report.html**, please take a look to see the run time, number of test cases with specific failed and passed errors