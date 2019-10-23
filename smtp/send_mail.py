import smtplib
import pandas as pd

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

address = open("contact/address.txt", "r")
password = open("contact/password.txt", "r")

MY_ADDRESS = address.read()
PASSWORD = password.read()


def create_html_gmail_message(message):
    return "<html>" + message + """\
        <br><br>
        

<div id=video>
    <video class="video" autoplay muted controls width="500" height="300">
        <source src="http://www.bad-kan.com/video/video_instructor.mp4" type="video/mp4">
    </video>
</div>



        <br><br>
        <div id="m_-651538905657960953Signature">
            <div id="m_-651538905657960953divtagdefaultwrapper" dir="ltr"
                style="font-size:12pt;color:#000000;font-family:Calibri,Helvetica,sans-serif">
                <p style="margin-top:0px;margin-bottom:0px;margin-top:0;margin-bottom:0"><span
                        id="m_-651538905657960953ms-rterangepaste-start"></span></p>
                <div
                    style="margin-bottom:30px;border:1px solid rgb(153,153,153);border-radius:10px;padding:20px;margin-right:20px;background-color:transparent;font-family:Trebuchet MS,Calibri,Arial,sans-serif;font-size:13px">
                    <div>
                        <div><img alt="horizontal bar" id="m_-651538905657960953OWAPstImg423488" style="max-width:100%"
                                src="http://www.bad-kan.com/images/horizontal_bar.png" data-image-whitelisted="" class="CToWUd">
                            <div class="yj6qo ajU">
                                <div id=":1w" class="ajR" role="button" tabindex="0" aria-label="Hide expanded content"
                                    aria-expanded="true" data-tooltip="Hide expanded content"><img class="ajT"
                                        src="//ssl.gstatic.com/ui/v1/icons/mail/images/cleardot.gif"></div>
                            </div><span class="HOEnZb adL">
                                <font color="#888888">
                                    <h3 style="margin-bottom:0px">Support Bad-kan</h3>
                                    <span>Badkan, Team support<br>
                                    </span><span><img alt="Badkan" id="m_-651538905657960953OWAPstImg607439"
                                            src="http://www.bad-kan.com/logo/favicon.png" data-image-whitelisted=""
                                            class="CToWUd" width="70" height="70"><br>
                                    </span><span>+972 53 708 4835<br>
                                    </span><a href="http://www.bad-kan.com" target="_blank"
                                        data-saferedirecturl="https://www.google.com/url?q=http://www.bad-kan.com&amp;source=gmail&amp;ust=1571834661701000&amp;usg=AFQjCNH6Cxsw5U0gfNYKzd-ID33gW6tbhw">http://www.bad-kan.com</a>
                                </font>
                            </span>
                        </div>
                        <div class="adL">
                        </div>
                    </div>
                    <div class="adL">
                    </div>
                </div>
                <div class="adL">
                    <span id="m_-651538905657960953ms-rterangepaste-end"></span><br>
                    <p style="margin-top:0px;margin-bottom:0px"></p>
                </div>
            </div>
            <div class="adL">
            </div>
        </div>
        </html>
        """

def create_html_message(message):
    return """\
        <!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
	xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="x-apple-disable-message-reformatting">
	<title></title>
	<link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet">

	<style>
		html,
		body {
			margin: 0 auto !important;
			padding: 0 !important;
			height: 100% !important;
			width: 100% !important;
			background: #f1f1f1;
		}

		/* What it does: Stops email clients resizing small text. */
		* {
			-ms-text-size-adjust: 100%;
			-webkit-text-size-adjust: 100%;
		}

		/* What it does: Centers email on Android 4.4 */
		div[style*="margin: 16px 0"] {
			margin: 0 !important;
		}

		/* What it does: Stops Outlook from adding extra spacing to tables. */
		table,
		td {
			mso-table-lspace: 0pt !important;
			mso-table-rspace: 0pt !important;
		}

		/* What it does: Fixes webkit padding issue. */
		table {
			border-spacing: 0 !important;
			border-collapse: collapse !important;
			table-layout: fixed !important;
			margin: 0 auto !important;
		}

		/* What it does: Uses a better rendering method when resizing images in IE. */
		img {
			-ms-interpolation-mode: bicubic;
		}

		/* What it does: Prevents Windows 10 Mail from underlining links despite inline CSS. Styles for underlined links should be inline. */
		a {
			text-decoration: none;
		}

		/* What it does: A work-around for email clients meddling in triggered links. */
		*[x-apple-data-detectors],
		/* iOS */
		.unstyle-auto-detected-links *,
		.aBn {
			border-bottom: 0 !important;
			cursor: default !important;
			color: inherit !important;
			text-decoration: none !important;
			font-size: inherit !important;
			font-family: inherit !important;
			font-weight: inherit !important;
			line-height: inherit !important;
		}

		/* What it does: Prevents Gmail from displaying a download button on large, non-linked images. */
		.a6S {
			display: none !important;
			opacity: 0.01 !important;
		}

		/* What it does: Prevents Gmail from changing the text color in conversation threads. */
		.im {
			color: inherit !important;
		}

		/* If the above doesn't work, add a .g-img class to any image in question. */
		img.g-img+div {
			display: none !important;
		}

		/* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
		/* Create one of these media queries for each additional viewport size you'd like to fix */

		/* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
		@media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
			u~div .email-container {
				min-width: 320px !important;
			}
		}

		/* iPhone 6, 6S, 7, 8, and X */
		@media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
			u~div .email-container {
				min-width: 375px !important;
			}
		}

		/* iPhone 6+, 7+, and 8+ */
		@media only screen and (min-device-width: 414px) {
			u~div .email-container {
				min-width: 414px !important;
			}
		}
	</style>


	<style>
		.primary {
			background: #0d0cb5;
		}

		.bg_white {
			background: #ffffff;
		}

		.bg_light {
			background: #fafafa;
		}

		.bg_black {
			background: #000000;
		}

		.bg_dark {
			background: rgba(0, 0, 0, .8);
		}

		.email-section {
			padding: 2.5em;
		}

		/*BUTTON*/
		.btn {
			padding: 5px 15px;
			display: inline-block;
		}

		.btn.btn-primary {
			border-radius: 5px;
			background: #0d0cb5;
			color: #ffffff;
		}

		.btn.btn-white {
			border-radius: 5px;
			background: #ffffff;
			color: #000000;
		}

		.btn.btn-white-outline {
			border-radius: 5px;
			background: transparent;
			border: 1px solid #fff;
			color: #fff;
		}

		h1,
		h2,
		h3,
		h4,
		h5,
		h6 {
			font-family: 'Poppins', sans-serif;
			color: #000000;
			margin-top: 0;
		}

		body {
			font-family: 'Poppins', sans-serif;
			font-weight: 400;
			font-size: 15px;
			line-height: 1.8;
			color: rgba(0, 0, 0, .4);
		}

		a {
			color: #0d0cb5;
		}

		table {}

		/*LOGO*/

		.logo h1 {
			margin: 0;
		}

		.logo h1 a {
			color: #000000;
			font-size: 20px;
			font-weight: 700;
			text-transform: uppercase;
			font-family: 'Poppins', sans-serif;
		}

		.navigation {
			padding: 0;
		}

		.navigation li {
			list-style: none;
			display: inline-block;
			;
			margin-left: 5px;
			font-size: 13px;
			font-weight: 500;
		}

		.navigation li a {
			color: rgba(0, 0, 0, .4);
		}

		/*HERO*/
		.hero {
			position: relative;
			z-index: 0;
		}

		.hero .overlay {
			position: absolute;
			top: 0;
			left: 0;
			right: 0;
			bottom: 0;
			content: '';
			width: 100%;
			background: #000000;
			z-index: -1;
			opacity: .3;
		}

		.hero .icon {}

		.hero .icon a {
			display: block;
			width: 60px;
			margin: 0 auto;
		}

		.hero .text {
			color: rgba(255, 255, 255, .8);
		}

		.hero .text h2 {
			color: #ffffff;
			font-size: 30px;
			margin-bottom: 0;
		}


		/*HEADING SECTION*/
		.heading-section {}

		.heading-section h2 {
			color: #000000;
			font-size: 20px;
			margin-top: 0;
			line-height: 1.4;
			font-weight: 700;
			text-transform: uppercase;
		}

		.heading-section .subheading {
			margin-bottom: 20px !important;
			display: inline-block;
			font-size: 13px;
			text-transform: uppercase;
			letter-spacing: 2px;
			color: rgba(0, 0, 0, .4);
			position: relative;
		}

		.heading-section .subheading::after {
			position: absolute;
			left: 0;
			right: 0;
			bottom: -10px;
			content: '';
			width: 100%;
			height: 2px;
			background: #0d0cb5;
			margin: 0 auto;
		}

		.heading-section-white {
			color: rgba(255, 255, 255, .8);
		}

		.heading-section-white h2 {
			font-family:
				line-height: 1;
			padding-bottom: 0;
		}

		.heading-section-white h2 {
			color: #ffffff;
		}

		.heading-section-white .subheading {
			margin-bottom: 0;
			display: inline-block;
			font-size: 13px;
			text-transform: uppercase;
			letter-spacing: 2px;
			color: rgba(255, 255, 255, .4);
		}


		.icon {
			text-align: center;
		}

		.icon img {}


		/*SERVICES*/
		.services {
			background: rgba(0, 0, 0, .03);
		}

		.text-services {
			padding: 10px 10px 0;
			text-align: center;
		}

		.text-services h3 {
			font-size: 16px;
			font-weight: 600;
		}

		.services-list {
			padding: 0;
			margin: 0 0 20px 0;
			width: 100%;
			float: left;
		}

		.services-list img {
			float: left;
		}

		.services-list .text {
			width: calc(100% - 60px);
			float: right;
		}

		.services-list h3 {
			margin-top: 0;
			margin-bottom: 0;
		}

		.services-list p {
			margin: 0;
		}

		/*BLOG*/
		.text-services .meta {
			text-transform: uppercase;
			font-size: 14px;
		}

		/*TESTIMONY*/
		.text-testimony .name {
			margin: 0;
		}

		.text-testimony .position {
			color: rgba(0, 0, 0, .3);

		}


		/*VIDEO*/
		.img {
			width: 100%;
			height: auto;
			position: relative;
		}

		.img .icon {
			position: absolute;
			top: 50%;
			left: 0;
			right: 0;
			bottom: 0;
			margin-top: -25px;
		}

		.img .icon a {
			display: block;
			width: 60px;
			position: absolute;
			top: 0;
			left: 50%;
			margin-left: -25px;
		}



		/*COUNTER*/
		.counter {
			width: 100%;
			position: relative;
			z-index: 0;
		}

		.counter .overlay {
			position: absolute;
			top: 0;
			left: 0;
			right: 0;
			bottom: 0;
			content: '';
			width: 100%;
			background: #000000;
			z-index: -1;
			opacity: .3;
		}

		.counter-text {
			text-align: center;
		}

		.counter-text .num {
			display: block;
			color: #ffffff;
			font-size: 34px;
			font-weight: 700;
		}

		.counter-text .name {
			display: block;
			color: rgba(255, 255, 255, .9);
			font-size: 13px;
		}


		/*FOOTER*/

		.footer {
			color: rgba(255, 255, 255, .5);

		}

		.footer .heading {
			color: #ffffff;
			font-size: 20px;
		}

		.footer ul {
			margin: 0;
			padding: 0;
		}

		.footer ul li {
			list-style: none;
			margin-bottom: 10px;
		}

		.footer ul li a {
			color: rgba(255, 255, 255, 1);
		}


		@media screen and (max-width: 500px) {

			.icon {
				text-align: left;
			}

			.text-services {
				padding-left: 0;
				padding-right: 20px;
				text-align: left;
			}

		}
	</style>
</head>

<body width="100%" style="margin: 0; padding: 0 !important; mso-line-height-rule: exactly; background-color: #222222;">
	<center style="width: 100%; background-color: #f1f1f1;">
		<div
			style="display: none; font-size: 1px;max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; mso-hide: all; font-family: sans-serif;">
			&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
		</div>
		<div style="max-width: 600px; margin: 0 auto;" class="email-container">

			<table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%"
				style="margin: auto;">
				<tr>
					<td valign="top" class="bg_white" style="padding: 1em 2.5em;">
						<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
							<tr>
								<td width="40%" class="logo" style="text-align: left;">
									<h1><a href="#">Badkan</a></h1>
								</td>
								<td width="60%" class="logo" style="text-align: right;">
									<ul class="navigation">
										<li><a href="#">Home</a></li>
										<li><a href="#">About</a></li>
										<li><a href="#">Works</a></li>
										<li><a href="#">Blog</a></li>
										<li><a href="#">Contact</a></li>
									</ul>
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr>
					<td valign="middle" class="hero bg_white"
						style="background-image: url(images/bg_1.jpg); background-size: cover; height: 400px;">
						<div class="overlay"></div>
						<table>
							<tr>
								<td>
									<div class="text" style="padding: 0 3em; text-align: center;">
										<h2>We Create Modern Website</h2>
										<p>A small river named Duden flows by their place and supplies it with the
											necessary regelialia. It is a paradisematic country, in which roasted parts
											of sentences fly into your mouth.</p>
										<div class="icon">
											<a href="#">
												<img src="images/002-play-button.png" alt=""
													style="width: 60px; max-width: 600px; height: auto; margin: auto; display: block;">
											</a>
										</div>
									</div>
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr>
					<td class="bg_white">
						<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
							<tr>
								<td class="bg_white email-section">
									<div class="heading-section" style="text-align: center; padding: 0 30px;">
										<h2>Our Services</h2>
										<p>A small river named Duden flows by their place and supplies it with the
											necessary regelialia.</p>
									</div>
									<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td valign="top" width="33.333%" style="padding-top: 20px;"
												class="services">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td class="icon">
															<img src="images/001-diet.png" alt=""
																style="width: 60px; max-width: 600px; height: auto; margin: auto; display: block;">
														</td>
													</tr>
													<tr>
														<td class="text-services">
															<h3>Branding</h3>
															<p>Far far away, behind the word mountains, far from the
																countries</p>
														</td>
													</tr>
												</table>
											</td>
											<td valign="top" width="33.333%"
												style="padding-top: 20px; background: rgba(0,0,0,.08);"
												class="services">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td class="icon">
															<img src="images/001-diet.png" alt=""
																style="width: 60px; max-width: 600px; height: auto; margin: auto; display: block;">
														</td>
													</tr>
													<tr>
														<td class="text-services">
															<h3>Design</h3>
															<p>Far far away, behind the word mountains, far from the
																countries</p>
														</td>
													</tr>
												</table>
											</td>
											<td valign="top" width="33.333%" style="padding-top: 20px;"
												class="services">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td class="icon">
															<img src="images/003-recipe-book.png" alt=""
																style="width: 60px; max-width: 600px; height: auto; margin: auto; display: block;">
														</td>
													</tr>
													<tr>
														<td class="text-services">
															<h3>Development</h3>
															<p>Far far away, behind the word mountains, far from the
																countries</p>
														</td>
													</tr>
												</table>
											</td>
										</tr>
									</table>
								</td>
							</tr>
							<tr>
								<td class="bg_light email-section" style="width: 100%;">
									<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td valign="middle" width="50%">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td>
															<img src="images/about.jpg" alt=""
																style="width: 100%; max-width: 600px; height: auto; margin: auto; display: block;">
														</td>
													</tr>
												</table>
											</td>
											<td valign="middle" width="50%">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td class="text-services"
															style="text-align: left; padding-left:25px;">
															<div class="heading-section">
																<h2>Business Strategy</h2>
																<p>A small river named Duden flows by their place and
																	supplies it with the necessary regelialia.</p>
																<p><a href="#" class="btn btn-primary">Read more</a></p>
															</div>
														</td>
													</tr>
												</table>
											</td>
										</tr>
									</table>
								</td>
							</tr>
							<tr>
								<td class="bg_white email-section">
									<div class="heading-section" style="text-align: center; padding: 0 30px;">
										<h2>Projects</h2>
										<p>A small river named Duden flows by their place and supplies it with the
											necessary regelialia.</p>
									</div>
									<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td valign="top" width="50%">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td style="padding-top: 20px; padding-right: 10px;">
															<a href="#"><img src="images/work-1.jpg" alt=""
																	style="width: 100%; max-width: 600px; height: auto; margin: auto; display: block;"></a>
														</td>
													</tr>
												</table>
											</td>
											<td valign="top" width="50%">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td style="padding-top: 20px; padding-left: 10px;">
															<a href="#"><img src="images/work-2.jpg" alt=""
																	style="width: 100%; max-width: 600px; height: auto; margin: auto; display: block;"></a>
														</td>
													</tr>
												</table>
											</td>
										</tr>
									</table>
									<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td valign="top" width="50%">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td style="padding-top: 20px; padding-right: 10px;">
															<a href="#"><img src="images/work-3.jpg" alt=""
																	style="width: 100%; max-width: 600px; height: auto; margin: auto; display: block;"></a>
														</td>
													</tr>
												</table>
											</td>
											<td valign="top" width="50%">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td style="padding-top: 20px; padding-left: 10px;">
															<a href="#"><img src="images/work-4.jpg" alt=""
																	style="width: 100%; max-width: 600px; height: auto; margin: auto; display: block;"></a>
														</td>
													</tr>
												</table>
											</td>
										</tr>
									</table>
								</td>
							</tr>
							<tr>
								<td valign="middle" class="counter"
									style="background-image: url(images/bg_1.jpg); background-size: cover; padding: 4em 0;">
									<div class="overlay"></div>
									<table>
										<tr>
											<td valign="middle" width="33.333%">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td class="counter-text">
															<span class="num">20</span>
															<span class="name">Clients</span>
														</td>
													</tr>
												</table>
											</td>
											<td valign="middle" width="33.333%">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td class="counter-text">
															<span class="num">1200</span>
															<span class="name">Projects</span>
														</td>
													</tr>
												</table>
											</td>
											<td valign="middle" width="33.333%">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td class="counter-text">
															<span class="num">100</span>
															<span class="name">Coffee Cups</span>
														</td>
													</tr>
												</table>
											</td>
										</tr>
									</table>
								</td>
							</tr>
							<tr>
								<td class="bg_white email-section">
									<div class="heading-section" style="text-align: center; padding: 0 30px;">
										<h2>Our Blog</h2>
										<p>A small river named Duden flows by their place and supplies it with the
											necessary regelialia.</p>
									</div>
									<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td valign="top" width="50%" style="padding-top: 20px;">
												<table role="presentation" cellspacing="0" cellpadding="10" border="0"
													width="100%">
													<tr>
														<td>
															<img src="images/blog-1.jpg" alt=""
																style="width: 100%; max-width: 600px; height: auto; margin: auto; display: block;">
														</td>
													</tr>
													<tr>
														<td class="text-services" style="text-align: left;">
															<p class="meta"><span>Posted on Feb 18, 2019</span>
																<span>Food</span></p>
															<h3>Business Key to Success</h3>
															<p>Far far away, behind the word mountains, far from the
																countries</p>
															<p><a href="#" class="btn btn-primary">Read more</a></p>
														</td>
													</tr>
												</table>
											</td>
											<td valign="top" width="50%" style="padding-top: 20px;">
												<table role="presentation" cellspacing="0" cellpadding="10" border="0"
													width="100%">
													<tr>
														<td>
															<img src="images/blog-2.jpg" alt=""
																style="width: 100%; max-width: 600px; height: auto; margin: auto; display: block;">
														</td>
													</tr>
													<tr>
														<td class="text-services" style="text-align: left;">
															<p class="meta"><span>Posted on Feb 18, 2019</span>
																<span>Food</span></p>
															<h3>Web Design Technique</h3>
															<p>Far far away, behind the word mountains, far from the
																countries</p>
															<p><a href="#" class="btn btn-primary">Read more</a></p>
														</td>
													</tr>
												</table>
											</td>
										</tr>
									</table>
								</td>
							</tr>
							<tr>
								<td class="bg_light email-section">
									<div class="heading-section" style="text-align: center; padding: 0 30px;">
										<h2>Our Team</h2>
										<p>A small river named Duden flows by their place and supplies it with the
											necessary regelialia.</p>
									</div>
									<table role="presentation" border="0" cellpadding="10" cellspacing="0" width="100%">
										<tr>
											<td valign="top" width="33.333%" style="padding-top: 20px;">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td>
															<img src="images/person_1.jpg" alt=""
																style="width: 100%; max-width: 600px; height: auto; margin: auto; margin-bottom: 20px; display: block;">
														</td>
													</tr>
													<tr>
														<td class="text-testimony" style="text-align: center;">
															<h3 class="name">Ronald Tuff</h3>
															<span class="position">Businessman</span>
															<p>Far far away, behind the word mountains</p>
														</td>
													</tr>
												</table>
											</td>
											<td valign="top" width="33.333%" style="padding-top: 20px;">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td>
															<img src="images/person_2.jpg" alt=""
																style="width: 100%; max-width: 600px; height: auto; margin: auto; margin-bottom: 20px; display: block;">
														</td>
													</tr>
													<tr>
														<td class="text-testimony" style="text-align: center;">
															<h3 class="name">Willam Clarson</h3>
															<span class="position">Businessman</span>
															<p>Far far away, behind the word mountains</p>
														</td>
													</tr>
												</table>
											</td>
											<td valign="top" width="33.333%" style="padding-top: 20px;">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td>
															<img src="images/person_3.jpg" alt=""
																style="width: 100%; max-width: 600px; height: auto; margin: auto; margin-bottom: 20px; display: block;">
														</td>
													</tr>
													<tr>
														<td class="text-testimony" style="text-align: center;">
															<h3 class="name">Willam Clarson</h3>
															<span class="position">Businessman</span>
															<p>Far far away, behind the word mountains</p>
														</td>
													</tr>
												</table>
											</td>
										</tr>
									</table>
								</td>
							</tr>
							<tr>
								<td class="bg_white email-section" style="width: 100%;">
									<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td valign="middle" width="50%">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td>
															<img src="images/bg_2.jpg" alt=""
																style="width: 100%; max-width: 600px; height: auto; margin: auto; display: block;">
														</td>
													</tr>
												</table>
											</td>
											<td valign="middle" width="50%">
												<table role="presentation" cellspacing="0" cellpadding="0" border="0"
													width="100%">
													<tr>
														<td class="text-services"
															style="text-align: left; padding-left:25px;">
															<div class="heading-section">
																<h2>Our Features</h2>
															</div>
															<div class="services-list">
																<img src="images/checked.png" alt=""
																	style="width: 50px; max-width: 600px; height: auto; display: block;">
																<div class="text">
																	<h3>Responsive</h3>
																	<p>A small river named Duden flows by their</p>
																</div>
															</div>
															<div class="services-list">
																<img src="images/checked.png" alt=""
																	style="width: 50px; max-width: 600px; height: auto; display: block;">
																<div class="text">
																	<h3>Responsive</h3>
																	<p>A small river named Duden flows by their</p>
																</div>
															</div>
															<div class="services-list">
																<img src="images/checked.png" alt=""
																	style="width: 50px; max-width: 600px; height: auto; display: block;">
																<div class="text">
																	<h3>Responsive</h3>
																	<p>A small river named Duden flows by their</p>
																</div>
															</div>
														</td>
													</tr>
												</table>
											</td>
										</tr>
									</table>
								</td>
							</tr>
							<tr>
								<td class="primary email-section" style="text-align:center;">
									<div class="heading-section heading-section-white">
										<h2>Get Ready For Modern Design</h2>
										<p>A small river named Duden flows by their place and supplies it with the
											necessary regelialia. It is a paradisematic country, in which roasted parts
											of sentences fly into your mouth.</p>
										<p><a href="#" class="btn btn-white-outline">Get Started</a></p>
									</div>
								</td>
							</tr>
						</table>
					</td>
				</tr>

			</table>
			<table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%"
				style="margin: auto;">
				<tr>
					<td valign="middle" class="bg_black footer email-section">
						<table>
							<tr>
								<td valign="top" width="33.333%" style="padding-top: 20px;">
									<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
										<tr>
											<td style="text-align: left; padding-right: 10px;">
												<h3 class="heading">About</h3>
												<p>A small river named Duden flows by their place and supplies it with
													the necessary regelialia.</p>
											</td>
										</tr>
									</table>
								</td>
								<td valign="top" width="33.333%" style="padding-top: 20px;">
									<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
										<tr>
											<td style="text-align: left; padding-left: 5px; padding-right: 5px;">
												<h3 class="heading">Contact Info</h3>
												<ul>
													<li><span class="text">203 Fake St. Mountain View, San Francisco,
															California, USA</span></li>
													<li><span class="text">+2 392 3929 210</span></a></li>
												</ul>
											</td>
										</tr>
									</table>
								</td>
								<td valign="top" width="33.333%" style="padding-top: 20px;">
									<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
										<tr>
											<td style="text-align: left; padding-left: 10px;">
												<h3 class="heading">Useful Links</h3>
												<ul>
													<li><a href="#">Home</a></li>
													<li><a href="#">About</a></li>
													<li><a href="#">Services</a></li>
													<li><a href="#">Work</a></li>
												</ul>
											</td>
										</tr>
									</table>
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr>
					<td valign="middle" class="bg_black footer email-section">
						<table>
							<tr>
								<td valign="top" width="33.333%">
									<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
										<tr>
											<td style="text-align: left; padding-right: 10px;">
												<p>&copy; 2018 Corporate. All Rights Reserved</p>
											</td>
										</tr>
									</table>
								</td>
								<td valign="top" width="33.333%">
									<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
										<tr>
											<td style="text-align: right; padding-left: 5px; padding-right: 5px;">
												<p><a href="#" style="color: rgba(255,255,255,.4);">Unsubcribe</a></p>
											</td>
										</tr>
									</table>
								</td>
							</tr>
						</table>
					</td>
				</tr>
			</table>
		</div>
	</center>

	<script async src="https://www.googletagmanager.com/gtag/js?id=UA-23581568-13"
		type="957bd51e4bb07702630b87d5-text/javascript"></script>
	<script type="957bd51e4bb07702630b87d5-text/javascript">
		window.dataLayer = window.dataLayer || [];

		function gtag() {
			dataLayer.push(arguments);
		}
		gtag('js', new Date());

		gtag('config', 'UA-23581568-13');
	</script>
	<script src="https://ajax.cloudflare.com/cdn-cgi/scripts/95c75768/cloudflare-static/rocket-loader.min.js"
		data-cf-settings="957bd51e4bb07702630b87d5-|49" defer=""></script>
</body>

</html>
    """

def send_mail(subject, message, client_mail):
    print(MY_ADDRESS)
    print(PASSWORD)
    print(client_mail)
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = MY_ADDRESS
    msg['To'] = client_mail
    msg.attach(MIMEText(create_html_message(message), 'html'))
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    s.send_message(msg)
    del msg
    s.quit()


def get_lines(filename):
    table = pd.read_csv(filename)
    first_line = 0
    for index, row in table.iterrows():
        if row["Name"] == "$@$":
            first_line = index + 2
    return first_line


def prepare_mail(row):
    subject = message = ""
    if row["Nationality"] == "French":
        subject = "Badkan: le nouveau correcteur"
        message += "<h1>Bonjour " + row["Title"] + ", </h1>"
        if row["University or website"] == "School":
            f = open("messages/french_school.txt", "r")
            message += f.read()
        elif row["University or website"] == "website e-learning":
            f = open("messages/french_learning.txt", "r")
            message += f.read()
    elif row["Nationality"] == "American":
        message += "<h1>Hello " + row["Title"] + ",  </h1>"
        subject = "Badkan: the new corrector"
        if row["University or website"] == "School":
            f = open("messages/american_school.txt", "r")
            message += f.read()
        elif row["University or website"] == "website e-learning":
            f = open("messages/american_learning.txt", "r")
            message += f.read()
    return subject, message


def read_csv(filename):
    first_line = get_lines(filename)
    table = pd.read_csv(filename, skiprows=range(1, first_line))
    for index, row in table.iterrows():
        subject, message = prepare_mail(row)
        client_mail = row["Email"]
        if "@" in client_mail:
            send_mail(subject, message, client_mail)


read_csv("emails.csv")
