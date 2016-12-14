# coding=utf-8
# Author: Lyy
# Email: henryly94@gmail.com
import re
html = '''
<!DOCTYPE>
<html>
<head>
    <title>SJTU Single Sign On</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0"/>
    <base href="/jaccount/"/>
    <link rel="icon" type="image/x-icon" href="image/favicon.png?v=20160919" />
    <link href="css/login.css?v=20160919" rel="stylesheet"/>
    <script>
        function setLocale(value) {
            var href = window.location.href;
            var regex = new RegExp("[&\\?]locale=");
            if(regex.test(href)) {
                regex = new RegExp("([&\\?])locale=\\w+");
                window.location.href = href.replace(regex, "$1locale=" + value);
            } else {
                if(href.indexOf("?") > -1)
                    window.location.href = href + "&locale=" + value;
                else
                    window.location.href = href + "?locale=" + value;
            }
        }
    </script>

</head>
<body>
<div id="page">
    <div id="header" class="clearfix">
        <div class="container">
            <div class="logo">
                <img src="image/sjtu.png?v=20160919" border="0"/>
            </div>
            <div class="i18n action-control">
                <a href="javascript:setLocale('zh')">涓枃</a> | <a href="javascript:setLocale('en')">EN</a>
            </div>
        </div>
    </div>
    <div id="content">
        <div class="container">
            <div class="login-bg"></div>
            <div class="login-layout">



<script src="https://mc.sjtu.edu.cn/httpsClient.js"></script>
<script>
    var subObj = msgCenter.create('f62c6351-d93d-4e98-9c73-c83aeadaf1ae');
    subObj.sub("100", function () {
        window.location.href = "weixinlogin?uuid=f62c6351-d93d-4e98-9c73-c83aeadaf1ae";
    });

    var switchLogin = function (switchDiv) {
        var div = document.getElementById('login-qr');
        if (div != null) {
            if (switchDiv.getAttribute('class') === 'login-switch') {
                switchDiv.setAttribute('class', 'login-switch pc');
                div.setAttribute('class', 'show');
                if (window.localStorage) {
                    window.localStorage.setItem("jaccount.login.type", "qrcode");
                }
            } else {
                switchDiv.setAttribute('class', 'login-switch');
                div.removeAttribute('class');
                if (window.localStorage) {
                    window.localStorage.setItem("jaccount.login.type", "password");
                }
            }
        }
    };

    var submitted = false;

    var checkForm = function (button) {

        if (submitted === true) {
            return false;
        }

        var warnUl = document.getElementById("ul_warn"),
                warnDiv = document.getElementById("div_warn"),
                user = document.getElementById("user"),
                password = document.getElementById("pass"),
                captcha = document.getElementById("captcha");

        if (warnDiv != null) {
            warnDiv.setAttribute("style", "display:none");
        }

        if (user.value == '') {
            document.getElementById("li_tip_no_user").setAttribute("style", "display:block");
            document.getElementById("li_tip_no_password").setAttribute("style", "display:none");
            document.getElementById("li_tip_no_captcha").setAttribute("style", "display:none");
            warnUl.setAttribute("style", "display:block");
            user.focus();
            return false;
        }

        if (password.value == '') {
            document.getElementById("li_tip_no_user").setAttribute("style", "display:none");
            document.getElementById("li_tip_no_password").setAttribute("style", "display:block");
            document.getElementById("li_tip_no_captcha").setAttribute("style", "display:none");
            warnUl.setAttribute("style", "display:block");
            password.focus();
            return false;
        }

        if (captcha.value == '') {
            document.getElementById("li_tip_no_user").setAttribute("style", "display:none");
            document.getElementById("li_tip_no_password").setAttribute("style", "display:none");
            document.getElementById("li_tip_no_captcha").setAttribute("style", "display:block");
            warnUl.setAttribute("style", "display:block");
            captcha.focus();
            return false;
        }

        submitted = true;
        warnUl.setAttribute("style", "display:none");
        button.setAttribute("class", button.getAttribute("class") + " submitted btn-secondary");
        return true;
    }
</script>
<div id="login-form">
    <div class="login-header">
        <div class="login-title">Login jAccount</div>
        <div id="login-switch" class="login-switch" onclick="switchLogin(this);"></div>
    </div>
    <ul id="ul_warn" class='warn-info' style="display: none">
        <li id="li_tip_no_user"><span class='icon i-warn'></span>Missing your account</li>
        <li id="li_tip_no_password"><span class='icon i-warn'></span>Missing your password</li>
        <li id="li_tip_no_captcha"><span class='icon i-warn'></span>Missing captcha</li>
    </ul>


    <form method="post" action="ulogin">
        <input type="hidden" name="sid" value="jalibtest04423">
        <input type="hidden" name="returl" value="CGTrzeeozZRiz9jYNbo04oINh/90hWU7O1m/5LVF6CxXnfabpDI3T7tKm2v/NO+dO84AMAW7Py6t">
        <input type="hidden" name="se" value="CFfurkPLCg8Cp518ZcczirR8+7R8XGbjjA==">
        <input type="hidden" name="v" value="">

        <div class="input-control">
            <span class="icon i-account"></span>
            <input class="form-input" type="text" id="user" name="user"
                   placeholder="Account" autocomplete="off">
        </div>
        <div class="input-control">
            <span class="icon i-pass"></span>
            <input class="form-input" type="password" id="pass" name="pass"
                   placeholder="Password" autocomplete="off">
        </div>
        <div class="input-control captcha-input">
            <span class="icon i-captcha"></span>
            <input class="form-input" type="text" id="captcha" name="captcha"
                   placeholder="Captcha" autocomplete="off">
            <img src="captcha?1476861611411" alt=""
                 onclick="this.src='captcha?'+Date.now()+Math.random()">
        </div>
        <div>
            <input type="submit" class="btn btn-primary form-submit"
                   value="SIGN IN"
                   onclick="return checkForm(this)">

        </div>
    </form>

        <div class="action-control">
            <a href="http://jaccount.sjtu.edu.cn/profile/pass.do">Reset Password</a>
            <a href="http://jaccount.sjtu.edu.cn/profile/apply!registerOption.do" class="pull-right">Sign Up</a>
        </div>

    <div id="login-qr">
        <div class="code">
            <img src="qrcode?uuid=f62c6351-d93d-4e98-9c73-c83aeadaf1ae" border="0"/>
        </div>
        <div class="qr-tips">
            --&nbsp;Scan QR code with your WeChat&nbsp;--
        </div>
    </div>
</div>
<script>
    if (window.localStorage) {
        var type = window.localStorage.getItem("jaccount.login.type");
        if (type == 'qrcode') {
            var switchDiv = document.getElementById('login-switch');
            if (switchDiv != null) {
                switchDiv.setAttribute('class', 'login-switch pc');
            }
            var qrDiv = document.getElementById('login-qr');
            if (qrDiv != null) {
                qrDiv.setAttribute('class', 'show');
            }
        }
    }
</script>

            </div>
        </div>
    </div>

    <div id="footer">
        <div class="container">
            <div class="contact">
                Xuhui campus: 4/F Hao Ran Hi-Tech Building 62932901 Minhang campus: 1/F Library & Information Building 34206060<br>



                        <span class="en">漏2016</span> <a href="http://net.sjtu.edu.cn">SJTU Network & Information Center</a> <a href="mailto:service@sjtu.edu.cn">service@sjtu.edu.cn</a>


            </div>
            <a class="net" href="http://net.sjtu.edu.cn"><img src="image/ja-net.png" border="0"></a>
        </div>
    </div>
</div>
</body>
</html>'''


if __name__ == '__main__':
    print re.findall('%s" value="(.*)">' % 'sid', html)[0]
    print re.findall('%s" value="(.*)">' % 'returl', html)[0]
    print re.findall('%s" value="(.*)">' % 'se', html)[0]
    print re.findall('%s" value="(.*)">' % 'v', html)[0]
    print re.findall('img src="captcha\?(.*)" alt', html)
