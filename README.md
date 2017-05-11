## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/sharad-vm/python/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/sharad-vm/python/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Titanic

<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />
<title>Titanic</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.6 (http://getbootstrap.com)
 * Copyright 2011-2015 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.2.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.2.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.2.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.2.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.2.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.2.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:
    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+
Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
@media (max-width: 991px) {
  #ipython_notebook {
    margin-left: 10px;
  }
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#login_widget {
  float: right;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  text-align: center;
  vertical-align: middle;
  display: inline;
  opacity: 0;
  z-index: 2;
  width: 12ex;
  margin-right: -12ex;
}
.alternate_upload .btn-upload {
  height: 22px;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: baseline;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI colors. */
.ansibold {
  font-weight: bold;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  border-left-width: 1px;
  padding-left: 5px;
  background: linear-gradient(to right, transparent -40px, transparent 1px, transparent 1px, transparent 100%);
}
div.cell.jupyter-soft-selected {
  border-left-color: #90CAF9;
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected {
  border-color: #ababab;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 5px, transparent 5px, transparent 100%);
}
@media print {
  div.cell.selected {
    border-color: transparent;
  }
}
div.cell.selected.jupyter-soft-selected {
  border-left-width: 0;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 7px, #E3F2FD 7px, #E3F2FD 100%);
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #66BB6A -40px, #66BB6A 5px, transparent 5px, transparent 100%);
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
@-moz-document url-prefix() {
  div.inner_cell {
    overflow-x: hidden;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  padding: 0.4em;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. We need the 0 value because of how we size */
  /* .CodeMirror-lines */
  padding: 0;
  border: 0;
  border-radius: 0;
}
/*
Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme
*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul {
  list-style: disc;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ul ul {
  list-style: square;
  margin: 0em 2em;
}
.rendered_html ul ul ul {
  list-style: circle;
  margin: 0em 2em;
}
.rendered_html ol {
  list-style: decimal;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
  margin: 0em 2em;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  background-color: #fff;
  color: #000;
  font-size: 100%;
  padding: 0px;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: 1px solid black;
  border-collapse: collapse;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  border: 1px solid black;
  border-collapse: collapse;
  margin: 1em 2em;
}
.rendered_html td,
.rendered_html th {
  text-align: left;
  vertical-align: middle;
  padding: 4px;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget {
  float: right !important;
  float: right;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 20ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  margin-top: 6px;
}
span.save_widget span.filename {
  height: 1em;
  line-height: 1em;
  padding: 3px;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  display: none;
}
.command-shortcut:before {
  content: "(command)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }
.ansi-bold { font-weight: bold; }
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}
div#notebook {
  overflow: visible;
  border-top: none;
}
@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Titanic---Data-Analysis">Titanic - Data Analysis<a class="anchor-link" href="#Titanic---Data-Analysis">&#182;</a></h1><h2 id="Introduction">Introduction<a class="anchor-link" href="#Introduction">&#182;</a></h2><p>As taken from Kaggle, 'The sinking of the RMS Titanic is one of the most infamous shipwrecks in history.  On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. This sensational tragedy shocked the international community and led to better safety regulations for ships.'</p>
<p>The data set used for this analysis is a subset of the complete data set and contains demographics and passenger information from 891 of the 2224 passengers and crew on board the Titanic.</p>
<p>For more information on the data set, visit <a href="https://www.kaggle.com/c/titanic/data">Kaggle</a>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Goal">Goal<a class="anchor-link" href="#Goal">&#182;</a></h2><p>The goal of this analysis is to analyze the data set and provide insights or identify patterns by investigating the data set.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Import-Packages">Import Packages<a class="anchor-link" href="#Import-Packages">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Import and load necessary packages</span>
<span class="kn">import</span> <span class="nn">re</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="kn">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="kn">as</span> <span class="nn">sns</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">matplotlib</span> <span class="kn">import</span> <span class="n">pyplot</span> <span class="k">as</span> <span class="n">pyplt</span>
<span class="kn">from</span> <span class="nn">matplotlib</span> <span class="kn">import</span> <span class="n">figure</span> <span class="k">as</span> <span class="n">fig</span>
<span class="kn">from</span> <span class="nn">matplotlib.gridspec</span> <span class="kn">import</span> <span class="n">GridSpec</span>

<span class="c1">#This is to plot the graphs within the same jupyter cell</span>
<span class="o">%</span><span class="k">matplotlib</span> inline

<span class="c1">#Adjusting the plot area size to accommodate bigger/wider graphs</span>
<span class="n">pyplt</span><span class="o">.</span><span class="n">rcParams</span><span class="p">[</span><span class="s1">&#39;figure.figsize&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">12</span><span class="p">,</span><span class="mi">6</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Load-data">Load data<a class="anchor-link" href="#Load-data">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Load dataset </span>
<span class="c1">#This loads the csv file to a pandas data frame</span>
<span class="c1">#Note that the path given below is where the csv file exists locally with in Python&#39;s current working directory</span>
<span class="c1">#Repoint the path as necessary to make sure the function read_csv is able to find the csv</span>

<span class="n">titanic</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;Udacity/P2/Titanic/titanic-data.csv&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Data-Exploration-and-Processing">Data Exploration and Processing<a class="anchor-link" href="#Data-Exploration-and-Processing">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Exploring the dataset for available columns and type of data</span>
<span class="n">titanic</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[3]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>0</td>
      <td>3</td>
      <td>Moran, Mr. James</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>330877</td>
      <td>8.4583</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>McCarthy, Mr. Timothy J</td>
      <td>male</td>
      <td>54.0</td>
      <td>0</td>
      <td>0</td>
      <td>17463</td>
      <td>51.8625</td>
      <td>E46</td>
      <td>S</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>0</td>
      <td>3</td>
      <td>Palsson, Master. Gosta Leonard</td>
      <td>male</td>
      <td>2.0</td>
      <td>3</td>
      <td>1</td>
      <td>349909</td>
      <td>21.0750</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)</td>
      <td>female</td>
      <td>27.0</td>
      <td>0</td>
      <td>2</td>
      <td>347742</td>
      <td>11.1333</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>1</td>
      <td>2</td>
      <td>Nasser, Mrs. Nicholas (Adele Achem)</td>
      <td>female</td>
      <td>14.0</td>
      <td>1</td>
      <td>0</td>
      <td>237736</td>
      <td>30.0708</td>
      <td>NaN</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>While the field Embarked, Survived and Pclass hold abbreviations for the port of embarkation, survival indicator and travel class, having descriptive names of the same look more meaningful especially in visulaizations.</p>
<p>Note that the port names were taken from the <a href="https://www.kaggle.com/c/titanic/data">Kaggle</a> website.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">ports</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;Cherbourg&quot;</span><span class="p">,</span> <span class="s2">&quot;Queenstown&quot;</span><span class="p">,</span> <span class="s2">&quot;Southampton&quot;</span><span class="p">]</span>
<span class="n">survival</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;Dead&quot;</span><span class="p">,</span> <span class="s2">&quot;Survived&quot;</span><span class="p">]</span>
<span class="n">travelclass</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;First Class&quot;</span><span class="p">,</span> <span class="s2">&quot;Second Class&quot;</span><span class="p">,</span> <span class="s2">&quot;Third Class&quot;</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1"># Creating descriptive labels</span>
<span class="c1"># Survival label</span>
<span class="n">titanic</span><span class="p">[</span><span class="s1">&#39;Survival&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">titanic</span><span class="o">.</span><span class="n">Survived</span><span class="o">.</span><span class="n">map</span><span class="p">({</span><span class="mi">0</span> <span class="p">:</span> <span class="n">survival</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="mi">1</span> <span class="p">:</span> <span class="n">survival</span><span class="p">[</span><span class="mi">1</span><span class="p">]})</span>

<span class="c1"># Ports label</span>
<span class="n">titanic</span><span class="p">[</span><span class="s1">&#39;Ports&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">titanic</span><span class="o">.</span><span class="n">Embarked</span><span class="o">.</span><span class="n">map</span><span class="p">({</span><span class="s2">&quot;C&quot;</span> <span class="p">:</span> <span class="n">ports</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s2">&quot;Q&quot;</span> <span class="p">:</span> <span class="n">ports</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="s2">&quot;S&quot;</span> <span class="p">:</span> <span class="n">ports</span><span class="p">[</span><span class="mi">2</span><span class="p">]})</span>

<span class="c1"># Travel class label</span>
<span class="n">titanic</span><span class="p">[</span><span class="s1">&#39;TravelClass&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">titanic</span><span class="o">.</span><span class="n">Pclass</span><span class="o">.</span><span class="n">map</span><span class="p">({</span><span class="mi">1</span> <span class="p">:</span> <span class="n">travelclass</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="mi">2</span> <span class="p">:</span> <span class="n">travelclass</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="mi">3</span> <span class="p">:</span> <span class="n">travelclass</span><span class="p">[</span><span class="mi">2</span><span class="p">]})</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Making sure the Embarked field has been updated</span>
<span class="n">titanic</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[6]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Survival</th>
      <th>Ports</th>
      <th>TravelClass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>Dead</td>
      <td>Southampton</td>
      <td>Third Class</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>Survived</td>
      <td>Cherbourg</td>
      <td>First Class</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>Survived</td>
      <td>Southampton</td>
      <td>Third Class</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>Survived</td>
      <td>Southampton</td>
      <td>First Class</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>Dead</td>
      <td>Southampton</td>
      <td>Third Class</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Taking a look at the basic stats</span>
<span class="n">titanic</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[7]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>714.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>446.000000</td>
      <td>0.383838</td>
      <td>2.308642</td>
      <td>29.699118</td>
      <td>0.523008</td>
      <td>0.381594</td>
      <td>32.204208</td>
    </tr>
    <tr>
      <th>std</th>
      <td>257.353842</td>
      <td>0.486592</td>
      <td>0.836071</td>
      <td>14.526497</td>
      <td>1.102743</td>
      <td>0.806057</td>
      <td>49.693429</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.420000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>223.500000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>20.125000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.910400</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>446.000000</td>
      <td>0.000000</td>
      <td>3.000000</td>
      <td>28.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>14.454200</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>668.500000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>38.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>891.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>80.000000</td>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>512.329200</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="How-many-people-were-on-the-ship-and-how-many-survived?">How many people were on the ship and how many survived?<a class="anchor-link" href="#How-many-people-were-on-the-ship-and-how-many-survived?">&#182;</a></h3><p>There were 891 passengers on Titanic and of them only 342 survived with an overall survival rate of 38%.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Get some basic counts and stats</span>

<span class="n">totalpassengers</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">titanic</span><span class="p">[</span><span class="s2">&quot;PassengerId&quot;</span><span class="p">]))</span>
<span class="n">survived</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">titanic</span><span class="p">[</span><span class="s2">&quot;Survived&quot;</span><span class="p">])</span>
<span class="n">overallsurvivalrate</span> <span class="o">=</span> <span class="n">format</span><span class="p">((</span><span class="n">survived</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">totalpassengers</span><span class="p">))</span> <span class="o">*</span> <span class="mi">100</span><span class="p">,</span> <span class="s1">&#39;0.2f&#39;</span><span class="p">)</span>

<span class="k">print</span> <span class="s2">&quot;Total Passengers on Titanic&quot;</span><span class="p">,</span> <span class="n">totalpassengers</span>
<span class="k">print</span> <span class="s2">&quot;Passengers Survived&quot;</span><span class="p">,</span> <span class="n">survived</span>
<span class="k">print</span> <span class="s2">&quot;Overall Survival Rate&quot;</span><span class="p">,</span> <span class="n">overallsurvivalrate</span><span class="p">,</span><span class="s2">&quot;%&quot;</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Total Passengers on Titanic 891
Passengers Survived 342
Overall Survival Rate 38.38 %
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="How-has-the-travel-class-on-the-ship-and-the-gender-of-passengers-affect-the-survival-rate?">How has the travel class on the ship and the gender of passengers affect the survival rate?<a class="anchor-link" href="#How-has-the-travel-class-on-the-ship-and-the-gender-of-passengers-affect-the-survival-rate?">&#182;</a></h3><p>From the bar plot below, it is evident that women in the 1st class had the highest survival rate at 10% followed by women in 2nd and 3rd classes at around 8% each. While the survival rate of men in 1st and 3rd class was around 5%, men in 2nd class seem to have the lowest survival rate.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Builds a bar plot with gender and travel class on the x-axis; number of people survived on the y-axis and survival rate in %</span>
<span class="n">genderplt</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">barplot</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="s2">&quot;Sex&quot;</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="s2">&quot;Survived&quot;</span><span class="p">,</span> <span class="n">hue</span> <span class="o">=</span> <span class="s2">&quot;TravelClass&quot;</span><span class="p">,</span> <span class="n">hue_order</span><span class="o">=</span> <span class="n">travelclass</span><span class="p">,</span> \
                        <span class="n">data</span> <span class="o">=</span> <span class="n">titanic</span><span class="p">,</span> <span class="n">estimator</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">,</span> <span class="n">ci</span> <span class="o">=</span> <span class="bp">None</span><span class="p">)</span>
<span class="n">genderplt</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">ylabel</span> <span class="o">=</span> <span class="s2">&quot;People Survived&quot;</span><span class="p">,</span> <span class="n">xlabel</span> <span class="o">=</span> <span class="s2">&quot;Gender&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">genderplt</span><span class="o">.</span><span class="n">patches</span><span class="p">:</span>
    <span class="n">height</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">get_height</span><span class="p">()</span>
    <span class="n">genderplt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">get_x</span><span class="p">()</span><span class="o">+</span><span class="n">p</span><span class="o">.</span><span class="n">get_width</span><span class="p">()</span><span class="o">/</span><span class="mf">2.</span><span class="p">,</span>
            <span class="n">height</span> <span class="o">+</span> <span class="mi">3</span><span class="p">,</span>
            <span class="s1">&#39;{:1.2f}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">((</span><span class="n">height</span> <span class="o">*</span> <span class="mi">100</span><span class="p">)</span><span class="o">/</span><span class="n">totalpassengers</span><span class="p">),</span>
            <span class="n">ha</span><span class="o">=</span><span class="s2">&quot;center&quot;</span><span class="p">)</span> 
<span class="n">genderplt</span><span class="o">.</span><span class="n">get_axes</span><span class="p">()</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="n">title</span> <span class="o">=</span> <span class="s2">&quot;Travel Class&quot;</span><span class="p">)</span>
<span class="n">genderplt</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span> <span class="o">=</span> <span class="s2">&quot;Survival Rate across Gender and Travel Class&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>c:\python27\lib\site-packages\matplotlib\artist.py:224: MatplotlibDeprecationWarning: get_axes has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  stacklevel=1)
</pre>
</div>
</div>

<div class="output_area"><div class="prompt output_prompt">Out[9]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.text.Text at 0x90bed90&gt;]</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
a1/xZu9ijLkXaAFMvyoVFhEREREREbkCfH2BudPASaCNMcbfuJn/tYG1wG3AimT5vwNqZW4VRURE
RERERK4snw7WrbVngTCgAy5w3wwsstZOAYoAvybb5SBQPFMrKSIiIiIiInKF+fQweK/ywCfAm7iF
5CKMMd8AQcDZZHnPAoEZObifnwc/v8vO7RcREZF/gSxZfLqfQv4BWbL44e+v+y4i1x6fDtaNMQ2B
Z4Di3l72td7V4f8P2EHKwDwQOJWRMvLly5HidQMiIiLy75Q7d/arXQXJZLlzZydv3hxXuxoiIhnm
08E6bgX4bd5APd5a4FVgGRCSLH8IcCAjBRw5clI96yIiIteJY8f0wpjrzbFjpzl69OTVroaISBLp
aUT09WD9V+BGY4y/tfa8d1t5YCewEghPlr82MDAjBVy8GMfFi3rVuoiIyPXgwoWLV7sKkskuXLjI
+fO67yJy7fH1YH0BMBSYZIwZCITiAvRwYC4wxBgzEpiIW4QuB/DhVaqriIiIiIiIyBXh06ttWGuP
4d6pXgRYBQwH+ltrJ1lrjwP3AfWA1UAN4B5rrca3iYiIiIiIyDXN13vWsdZuAe5OI201UC1zayQi
IiIiIiLyz/LpnnURERERERGR65GCdREREREREREfo2BdRERERERExMcoWBcRERERERHxMQrWRURE
RERERHyMgnURERERERERH6NgXURERERERMTH+Px71kVERERERK4nhw4d5M0332Ddup/InTsPLVo8
RsuWrVLN++OP/yMiYgS//rqfChUq8corr1K0aDEAYmNjGTt2FN9++zUej4e6devz4ovdCAzMlpmn
I3+RetZFRERERER8SO/ePQkKCiIyciadO3fjnXfeZvnyJSnyHTwYTa9eL9G06YNMmjSDPHmCCQ/v
kZAeGTmRdet+ZvjwMQwdOop1635mwoSxmXgm8ncoWBcREREREfERx48f55dfNvLf/z5DsWLFuf32
+tSsWYs1a35MkXfhwo8pX/4mWrZ8nNKl/0OvXn2Jjv6Vn3/+CYCVK7/ngQceoly5UEJDy/PQQ4+k
ehzxTQrWRUREREREfERgYCDZsmXns88WcP78efbsiWLDhnWUKxeaIu+mTRu45ZYqifbNRrlyoWzc
uB6A4OBgliz5huPHj3P8+HGWLl2c6nHENylYFxERERER8REBAQF06/Yy8+fPpWHDOjzxRAtuu60O
9957f4q8MTG/UaBAwSTb8uXLx+HDhwB4/vnO/Prrfu67ryH33deQY8eO0a3bK5lyHvL3KVgXERER
ERHxIVFRu7j99nq88840evXqy5Il3/DVV5+nyHfmzBkCAgKSbMuaNYDY2HMA7Nu3h5CQIkRETGDE
iLc4dy6WMWNGZMo5yN+n1eBFRERERER8xOrVq/j004+ZN+8zAgICKFculMOHDzFtWiSNGjVJkjcg
IIDY2Ngk286diyVXrtycOnWSN954nYiI8YSG3gRAz569CQt7jnbtOpAvX/5MOyf5a9SzLiIiIiIi
4iO2bt1C8eIlk/SYly1rOHjwQIq8BQsW4siRmCTbYmJiyJ8/P7t3R3H27BnKlCmbkFaunOHixYsc
OnTwnzsBuWIUrIuIiIiIiPiIAgUKsm/fXs6fP5+wbffuXRQpUjRF3goVKrJ+/c8Jv585c4Zt2yw3
31wpYS57VNTOhPSoqCg8Hk+qxxLfo2BdRERERMTHLVq0kLp1b6VevRpJ/q5fv2aq+efPn0PLlg9y
99316d79RX79dX+S9MmTJ/DAA3dz330NGTp0IOfOncuM05B0qFOnLv7+/gwZ8jp79+5hxYplvPvu
VFq0aEVcXBxHjsQkBPL33fcAGzasY+bMaezatZNBg/pRtGgxKleuSsGChahZsxZDhw7E2i1s2fIL
w4YN4q677iY4OM9VPktJD09cXNzVrsNVdfjw8ev7AoiIiFxH1q5dw/AZy8hfpMzVropkgpgDO+je
uh5VqlS72lX522JjYzl58kTC7+fOnePFFzty++31CAvrkiTv//73A3369OS11wZRokRJxo+PYN++
fUydOguAGTOm8uGHs+jffzDZs2fntdde5Y477qJ9+xcy9Zwkbbt3RzF69Jv88ssm8uTJS/PmLWne
/DGiow/QsuWDjBkznsqVqwLufo8e/SaHDx+iYsVbePnlVwkJKQLAiRMneOutkfzwwwrAQ716dxAW
1pnAwGxX8ewEoGDBXJ7L5dECcyIiIiIiPi4gIICAgHwJv8+YMQWADh3CUuRdufJ7atSoRa1adQBo
2/Y5/vvfVhw79gc5c+biww9nERbWJaER45ln2rNo0aeZcBaSXqVKlWbEiLdSbA8JKcKyZauSbKtZ
sxazZs1N9Tg5c+akZ8/e/0gd5Z+nYfAiIiIiIteQY8eOMXPmdDp27IS/f8q+t+DgYNatW8uePVGc
P3+eRYs+pWjRYuTKlZudO3dw7Ngf1K1bPyF/o0ZNGDEiIjNPQUTSQT3rIiIiIiLXkI8+mk3BggWp
X/+OVNMfeeRRVq9exRNPtMDPz4/s2YN4++138Hg8HDiwn1y5crN+/TomThzL77//ToMGd9Kx44tk
zZo1k89ERC5FPesiIiIiIteQhQs/oXnzx9JMP3z4ELGxsbz22kAmTJhClSpV6devN+fOneP06dOc
OXOaCRPeolOnbvTq1ZfvvlvO22+PycQzEJH0ULAuIiIiInKN2Lx5E7/9doiGDRunmWf48Ddo0OBO
GjZsTGjoTfTp8zqHDh1k+fKlZMmShdjYWLp0eZkqVapRvXoNwsK6sGDBR5l4FiKSHgrWRURERESu
Ef/73w/ccksVcubMmWYeazdz443lEn7Pnj07xYuXIDr6APnzFwCgZMlSCeklS5YmNjaWo0eP/nMV
F5EMU7AuIiIiInKN+OWXTVSqVPmSeQoUKEhU1M6E32NjYzlw4FeKFStGuXIGf39/tm/fmpAeFbWT
oKAggoOD/7F6i0jGKVgXEREREblG7Nq1g1Kl/pNk28WLFzlyJIbz588DcP/9zZg+PZLvv1/Bnj27
GTp0IDly5KB27boEBeXg/vubMWrUMDZt2sjGjesZN+4t7r//Ifz8FBqI+BKtBi8iIiIico04evQI
uXPnSrLt0KGDtGz5IGPGjKdy5aq0atUagFGjhnHs2DEqVqzEqFFvJ6z23qlTN8aNG8NLL3UG4O67
76V9+xcy90RE5LI8cXFxV7sOV9Xhw8ev7wsgIiJyHVm7dg3DZywjf5EyV7sqkgliDuyge+t6VKlS
7WpXRUQkiYIFc3kul0djXURERERERER8jIJ1ERERERERER+jYF1EROT/27vzMLuqOl3AXyWBYICE
BLplnkQWGGZUxAHBGQdEb6OCimADDi2DA4OACEZlFBQZRL2CtNqtXq9Dw8V5AAVE1LQQZdFICMhM
AgkgJCRV949TwUolaKVyqs6uqvd9njyps846e/92is2ur9baawMANIwF5gAAgBFv0aJFmTXrhk6X
wTCaPn37rL766p0uY8gI6wAAwIg3a9YNueKUE7PZlKmdLoVhMGf+g8lHPz6qF5AU1gEAgFFhsylT
s/V663W6DGgL96wDAABAwwjrAAAA0DDCOgAAADSMsA4AAAANI6wDAABAwwjrAAAA0DAe3QYAwKjU
vWRxar2p02UwTHyvGW2EdQAARqWHH7w3X595Tda5f91Ol8IwuGPmrTk4T+90GdA2wjoAAKPWOhut
m3FJY5EAACAASURBVPW2EODGgofumpvc1ekqoH3csw4AAAANI6wDAABAwwjrAAAA0DDCOgAAADSM
sA4AAAANI6wDAABAwwjrAAAA0DDCOgAAADSMsA4AAAANI6wDAABAwwjrAAAA0DDCOgAAADSMsA4A
AAANI6wDAABAwwjrAAAA0DDCOgAAADSMsA4AAAANI6wDAABAwwjrAAAA0DDCOgAAADSMsA4AAAAN
I6wDAABAwwjrAAAA0DDCOgAAADSMsA4AAAANI6wDAABAwwjrAAAA0DDCOgAAADSMsA4AAAANI6wD
AABAwwjrAAAA0DDCOgAAADSMsA4AAAANI6wDAABAwwjrAAAA0DDCOgAAADSMsA4AAAANM2EgnUop
mw50g7XW2wdfDgAAADCgsJ7ktiQ9A+w7fnClrFgpZfUk5yTZP8nCJF+qtZ7Q+97OSS5Msn2SG5O8
p9b6u3buHwAAAIbbQKfB75XkJb1/3p/kwSQfSPK8JLsmeXeSu5O8dwhqPDfJS5O8PMkBSQ4tpRxa
SpmU5PIkv0iyS5JrklxeSnnaENQAAAAAw2ZAI+u11l8s/bqU8ukkh9Zav92ny8xSyt1JzkxyUbuK
K6VMTfLOJC+ptf62t+2sJLslWZzkr7XWY3u7H1VKeXWS/ZJc2q4aAAAAYLgNZoG5kmTWCtpvSTLg
e9sH6IVJHqq1/nJpQ631jFrrIWmN6v+yX/9fJdm9zTUAAADAsBroPet9/SHJkaWU99Vae5KklDIh
yfFJrmtncUm2THJbKeXtvdtfPcnFST6RZIO07lPv694k09tcAwAAAAyrwYT1o5P8IMmrSim/T9KV
5DlJ1kzrnvZ2WivJ1kkOTXJQWgH9oiSPJpmU1oJzfS1MMnFldjBuXFfGjeta5UIBgOYbP95TawFG
i/Hjx2XChNH7//WVDuu11qtKKdOTHJZku97mS5JcWGu9u421Ja370tdOckCt9S9JUkrZLK2F7G7O
8sF8YpK/rswOpk1bM11dwjoAjAWTJ1uHFmC0mDz5aZk6dc1OlzFkBjOynlrr7CQfLqVMTLJo6XT4
IXB3kseXBvWlu0+ySZKfJVm/X//1ez8zYPPmPWpkHQDGiAULHut0CQC0yYIFj+XBBx/tdBmDMpBf
MgwqrJdS3p3kmLQWlNu6lPKhJHfVWj8+mO39HdckWaOUslWt9ZbetmclmZ3k2iQf7tf/+Wndzz5g
3d096e4eqt81AABNsmRJd6dLAKBNlizpzuLFo/f/6ys9wb+UckCS09J6PNqi3uabkpxQSvlgG2tL
rfV/0nqW+iWllB1KKa9McmySC5J8K8k6pZRzSinbllI+k9Z9899oZw0AAAAw3AZzN/6HkhxZaz05
yZIkqbWem+TfkryrfaU96a1pPRbuqrTujf9srfX8WuvDSV6TZI8k1yd5bpK9a63mtwEAADCiDWYa
fEly5Qraf5bk/FUrZ3m9ofyg3j/937s+ya7t3icAAAB00mBG1u9JK7D39/wkd61aOQAAAMBgwvpF
Sc4vpeyT1jPWS++Cc59J8qV2FgcAAABj0WCes35GKWWdJP+ZZI20FoBbnORzSU5tb3kAAAAw9gz2
OevHl1I+ntZj1MYluanWuqCtlQEAAMAYtdJhvZQyO8mXk3y5d4E3AAAAoI0Gc8/6xUnekuSWUsov
SikHlVLWbHNdAAAAMGatdFivtX6s1rpNkuclmZnWfer3lFIuKaXs2eb6AAAAYMwZzMh6kqTW+pta
65FJNkpybJI3JPlJuwoDAACAsWpQC8wlSSllkyQHJHlrWgvN/TytKfIAAADAKhjMAnOHpRXQX5Dk
tvxtsbnb21saAAAAjE2DGVn/VJL/k+QjtdYr21wPAAAAjHmDCevr11ofbXslAAAAQJIBhvVSypeS
HFlrfTjJZ0spT9m31vrONtUGAAAAY9JAR9a3SDK+9+stk/QMTTkAAADAgMJ6rXWvPl/vOWTVAAAA
AINaDX52/rYC/Oz2lwQAAABj27hBfObiJG9Jcksp5RellINKKWu2uS4AAAAYs1Y6rNdaP1Zr3SbJ
85LMTHJqkntKKZeUUvZsc30AAAAw5gxmZD1JUmv9Ta31yCQbJTk2yRuS/KRdhQEAAMBYNZjnrCdJ
SimbJDkgyVuTPCvJz9OaIg8AAACsgsEsMHdYWgH9BUluy98Wm7u9vaUBAADA2DSYkfVPJflmko/U
Wq9scz0AAAAw5g0mrH8zySdqrX9udzEAAADA4BaYe2OSJe0uBAAAAGgZTFj/f0kOL6Ws3e5iAAAA
gMFNg98wyVuSHFVKuS/JY33frLVu2Y7CAAAAYKwaTFj/We8fAAAAYAisdFivtZ4yFIUAAAAALYN5
zvqBf+/9Wuulgy8HAAAAGMw0+Eueov3xJH9JIqwDAADAKhjMNPhlVpAvpYxPsnWSC5J8vk11ATAK
XHnlz3PCCUenq6srPT096erqyotf/JLMmHHacn0vv/x7+drXLs19992XLbd8Rt73vqOy/fY75p57
7s5+++2zzDZ6enqSJOed94XsuONOw31YAABDbjAj68uotS5J8qdSygeSfDPJf6xyVQCMCrfddmte
+MI9cswxJyZpBezVV199uX7XXnt1zjnnjBx33Eey7bbTc8UVl+Xoo4/MV7/6f/LP//z0fO97P1im
/7nnnp277roz2223/XAcBgDAsBvMc9afSndaj3UDgCTJnDmzs8UWz8jUqVMzdeq0TJ06LWuuudZy
/a644rK8+tWvy8te9spstNHGOeSQd2fatHVzzTW/zLhx45787NSp0/KXv9yRX/ziZznxxFMyfvz4
DhwVAMDQa9cCc5OTHJrk16tcEQCjxuzZs/PsZ+/2D/u97W3vyKRJay7X/sgjjyzXdtFF52effd6Q
TTbZtC01AgA0UbsWmHsiyTVJ3rtK1QAwqtxxx5z8+tfX5NJLv5Tu7u7stdfLcsgh786ECctefp75
zLLM62uvvTp/+csd2XXX5yzT/oc/zMysWTfk5JM/OeS1AwB00iovMAcAK3LPPfdk4cKFmThxYmbM
OD13331nzjnnzCxatDBHHPHBp/zcnXf+Jaeeekpe8Yq9lwvx//Vf38kee+yV9dZbb6jLBwDoqFVa
YK6UMiHJDknurbXe2Z6SABgN1l9//Vx++U+y9tprJ0m22uqZ6e7uzowZJ+Xwwz+Qrq6u5T5z++1z
8v73/1s23njTHHPMCcu8t2TJklx11S/y0Y/OGJb6AQA6acCj5KWUt5VSri+lbNr7etsktyT5TZI5
pZQv9j7GDQCS5MmgvtRmm22RRYsWZcGC+cv1vfXWP+fwww/L05++fs488zPLrRp/441/yJIlSwZ0
DzwAwEg3oLBeSvlfSb6c5H+S/LW3+ZIk6yR5XZIXJ3lhkiPbXyIAI9F1112b17zmpVm4cOGTbTff
XDN58pRMmbLOMn3nzn0gH/zg4dlkk81yzjnnZdKkSctt749/nJVtttk2q6222pDXDgDQaQMdWT8i
ycdqrfvXWh8opWyX5DlJzq+1/r9a66+SnJjkoCGqE4ARZrvtdsjEiWvk9NM/nttvn5NrrvlVLrzw
3Lz1re9IT09P5s2bm8WLFydJzjvv0+nu7s5xx30kjz76aObNm5t58+bmsccee3J7s2f/OZtttkWn
DgcAYFgN9J71HZO8p8/rlyTpSfJffdpmJtmqTXUxhlx55c9zwglHp6urKz09Penq6sqLX/ySzJhx
2nJ9f/ObX+eznz07d911Z6ZP3yHHHntCNtxwoyTJww8/nFe/+iVPbidJpkxZJ5dd9qNhPR6gZdKk
STn77PNy7rmfyqGHHphJk9bM61//xuy//9tyzz13Z7/99slnP3tRdtppl1x11c+zaNGiHHDA/1pm
GwcffGgOPvjQJMmDD87LVltt3YlDAQAYdgMN66vnb9Pfk2SPJI+kdb/6UqslWdSmuhhDbrvt1rzw
hXvkmGNOTOt3QFnuXtUkuffee3L88Ufn0EPfnec+d/dcfPHn8+EPfyhf/vJ/PLmdKVPWyb//+zee
3E5Xl4cXQCdtvvkWOfvs85ZrX3/9DXLVVX+7hPz4x7/8h9s688zPtLU2AIAmG2hYr0l2TXJbKWWN
JC9L8tNa65I+fV6b5OY218cYMGfO7GyxxTMyderUv9vvssu+m223fVbe9KYDkiTHH//R7LPPKzNz
5u+y0067ZM6c2dlkk03/4XYAAACabqDDjhcnObeUcmSSryeZnOTCJCmlrF5K2S+te9b/fUiqZFSb
PbsVsv+RWbNuyI477vzk64kT18jWW2+TG2/8w0ptBwAAoOkGNLJeaz23lLJeWoG8O8kHaq0/7H37
M0nelVZQP39IqmRUu+OOOfn1r6/JpZd+Kd3d3dlrr5flkEPenQkTlv3Pc+7cB7Leev+0TNu0adNy
//33JWmN0C9evDiHHvqOPPDA/dlhh51yxBEfyLrrrjdsxwIAANAOA50Gn1rrSUlOWsFbFyS5oNZ6
Q9uqYsy45557snDhwkycODEzZpyeu+++M+ecc2YWLVqYI4744DJ9H3/88eXuZV9ttdWzaNETSZI5
c+Zk6tSpOfLID6WnpzsXXXR+jjnm/fniFy9NV1fXsB0TAADAqhpwWH8qQjqrYv3118/ll/8ka6+9
dpJkq62eme7u7syYcVIOP/wDy4Ts1VdfPYsWLbuG4RNPLMraa09OknzlK99IV1fXk4F+xozTs+++
r8qsWTdmu+22H6YjAgAAWHWWyqbjlgb1pTbbbIssWrQoCxbMX6b9n/7pnzNv3txl2ubOnZt11103
STJx4sRlRt6nTp2ayZOn5IEH7huiygEAAIaGsE5HXXfdtXnNa16ahQsXPtl28801kydPyZQp6yzT
d/r07fOHP8x88vXjjz+e//mfmu222yF//eujefWrX5qZM3/35Pv3339f5s9/KJtuuvmQHwcAAEA7
Cet01Hbb7ZCJE9fI6ad/PLffPifXXPOrXHjhuXnrW9+Rnp6ezJs3N4sXL06SvOY1++SGG/47X/3q
lzN79q355CdPyYYbbpSddtolkyatmR133Cnnnvup3HTTH1PrTTn55BPyvOe9IFtu+YwOHyUAAMDK
EdbpqEmTJuXss8/LQw89mEMPPTBnnPGJvP71b8z++78t9957T/bdd+8nH822/vob5BOfODOXX/69
HHbYO/LIIw/n1FM/9eS2TjjhlGy99TY5+uijcuSR786GG26Uk06a0alDAwAAGLRBLTBXStk7yTFJ
SpLdkxyc5JZa61faWBtjxOabb5Gzzz5vufb1198gV1553TJtu+22e772tW+tcDtrrbVWjjvuI0NS
IwAAwHBa6ZH1UsrLk3w7yZwkU5OMT7JakktKKQe2tzwAAAAYewYzDf6UJMfVWg9KsjhJaq0nJDk+
ydHtKw0AAADGpsFMg98+ydtX0P7NJCevUjUAY9yiRYsya9YNnS6DYTR9+vbLPHYSACAZXFifn2TD
JH/u1z49ybxVrghgDJs164ZcccqJ2WzK1E6XwjCYM//B5KMfz84779rpUgCAhhlMWP9qkk+XUg5O
0pNkrVLKq5Kcl+Tr7SwOYCzabMrUbL3eep0uAwCADhpMWD8xySZJZva+/n2SriSXJTmhTXUBAADA
mLXSYb3W+kSSA0opJyXZKa1F6m6stf6x3cUBAADAWDSo56wnSa31liS3tLEWAAAAIAMM66WU7rTu
T/+Haq3jV6kiAAAAGOMGOrL+zgwwrAMAAACrZkBhvdZ6yRDXAQAAAPQa1D3rpZT9khyVZPskS5L8
LsnptdYftrE2nsKiRYsya9YNnS6DYTR9+vZZffXVO10GAAAwTFY6rJdS3pnk80m+meQ/k4xP8oIk
l5dS9qu1fqe9JdLfrFk35KRP/0emrLtRp0thGMyfe2c+dlSy8867droUAABgmAxmZP3DST5Ua/10
n7ZPl1KOTnJKEmF9GExZd6Osu8EzOl0GAAAAQ2DcID6zUZLLV9D+7STPXLVyAAAAgMGE9SuTvHkF
7a9I8stVKwcAAAAYzDT4q5KcWEp5dpKfJ3kiyXOS7J/kklLKSUs71lo/1o4iAQAAYCwZTFg/JMk9
SXbs/bPUXWmNri/Vk0RYBwAAgJW00mG91rrFUBQCAAAAtAz2OetdSV6Z1nPWn0gyK8lPa61L2lgb
AAAAjEmDec76tCQ/SLJrkofSWqRucpLfllJeXmt9qL0lAgAAwNgymNXgz0oyKclOtdZptdZ1kuyc
ZI0kp7azOAAAABiLBhPWX5fkvbXWPyxtqLX+d5LDk7yhXYUBAADAWDWYsL5aWqvB93dPWtPhAQAA
gFUwmLD+2yTvWUH7e5P8ftXKAQAAAAazGvyJSX5WStk9ya/Sep76i9J65vqr2lgbAAAAjEkrPbJe
a70myR5Jbkvr8W17J7k1yYtqrT9ra3UAAAAwBg3qOeu11uuSvLnNtQAAAAAZZFgvpeyd5Ogk2yTZ
PcnBSW6ptX6ljbUBAADAmLTS0+BLKS9P8u0ktyeZmmR8WivEX1JKObC95S2378tLKV/q83rnUsq1
pZRHSym/LqXsMpT7BwAAgOEwmNXgT0lyXK31oCSLk6TWekKS49MabR8SpZS3pHV//NLXk5JcnuQX
SXZJck2Sy0spTxuqGgAAAGA4DCasb5/kv1bQ/s0kz1i1claslDI1yRlJruvT/JYkf621Hltbjkry
cJL9hqIGAAAAGC6DCevzk2y4gvbpSeatWjlP6awklyb5U5+23ZL8sl+/X6V1Dz0AAACMWIMJ619N
8ulSyg5pPWN9rVLKq5Kcl+Tr7SwuSUopL0nrOe4z+r21QZK7+rXdm2TjdtcAAAAAw2kwq8GfmGST
JDN7X/8+SVeSy5Kc0Ka6kiSllIlJLkzy3lrrwlJK37cnJVnY7yMLk0xcmX2MG9eVceO6VqnO4TZ+
/GB+x8JINn78uEyY4Ps+Fji/xx7n9/ByjgGMHqP9GrrSYb3W+kSSA0opJyXZKa3R+RtrrX9sd3FJ
Tk5yfa31xyt47/EsH8wnJvnryuxg2rQ109U1ssL65MnW0BtrJk9+WqZOXbPTZTAMnN9jj/N7eDnH
AEaP0X4NHXBYL6VsnOQNaYXkK2qttyS5ZagK6/XmJE8vpTzc+3piby3/kuRrSdbv13/9JHevzA7m
zXt0xI2sL1jwWKdLYJgtWPBYHnzw0U6XwTBwfo89zu/h5RwDGD1G8jV0IL9kGFBYL6W8MMn305p6
niQPl1L2q7X+cPDlDciL03qG+1JnpHWf/LG97x3br//zk3xiZXbQ3d2T7u6eValx2C1Z0t3pEhhm
S5Z0Z/Fi3/exwPk99ji/h5dzDGD0GO3X0IGOrM9I8pMk706yJK3F5M5Ost0Q1ZUkqbXe0fd17wh7
T6311lLK/UlOLaWck+TzvbWtmeQbQ1kTAAAADLWB3o2/S5IP11rvrrXel+T9SbYtpaw9dKX9fbXW
h5O8NskeSa5P8twke9dazW8DAABgRBvoyPpaSeYufVFrvbOUsijJtCQPP+Wn2qzWenC/19cn2XW4
9g8AAADDYaAj611p3Sve1+Ik49tbDgAAADB6H0oHAAAAI9TKPGf9g6WUvuvir5bkiFLKvL6daq0f
a0tlAAAAMEYNNKzfnuRN/druTvL6fm09SYR1AAAAWAUDCuu11s2HuA4AAACgl3vWAQAAoGGEdQAA
AGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgY
YR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0A
AAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAa
RlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgH
AACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACA
hhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHW
AQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAA
oGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGE
dQAAAGgYYR0AAAAaRlgHAACAhhHWgWG3aNGiHHjgmzNz5u+ess91112bgw46IC9/+R55//v/Lbff
PmeF/S655Iv55CdPGapSAQCgI4R1YFgtWrQoJ598Qm67bfZT9rn11j/nmGOOyh577JkvfekreeYz
S4488j15/PHHl+n3ox99Pxdf/IWhLhkAAIadsA4Mm9tum513veug3H33nX+333e/+61st90Oeec7
D8smm2ya9773iKy11lr54Q+vSJIsWbIkZ511ak4//ePZeONNhqN0AAAYVsI6MGxmzvxtdt31ufnc
5y5OT0/PU/a76647M3369su0bbnlM3LjjX9Ikjz22GO59dY/5/Ofv2S5fgAAMBpM6HQB/0gpZcMk
5ybZK8lfk3wjyYdrrYtKKZsn+UKS3ZPcluT9tdYfdahU4B/Yd99/GVC/qVOn5YEH7lum7b777s3k
yVOSJGuttVYuuOCLba8PAACaYiSMrH8ryRpJXpDkLUlel2RG73vfTXJXkl2TfCXJt0spG3eiSKB9
XvrSV+RnP/tJrr76l1myZEmuuOKy/OlPf8wTTyzudGkAADAsGj2yXkopSZ6b5Om11gd6205KcmYp
5ftJtkiyW6318SSnlVJemuSdST7WqZqBVbfbbrvn4IMPzYknHpMlS5Zkl12enb33fm0eeeSRTpcG
AADDotFhPck9SfZeGtT7mJLkeUl+1xvUl/plWlPigRHu7W8/OPvv//Y88sgjWWeddXLSSR/OBhts
0OmyAABgWDR6GnytdX6t9YdLX5dSupK8L8lPkmyQ1hT4vu5NYho8jHA//vEPcu65n8qECROyzjrr
ZOHCx/O7312fnXd+dqdLAwCAYdH0kfX+zkyyc5LnJPlAkoX93l+YZOLKbHDcuK6MG9fVnuqGyfjx
jf4dC0Ng/PhxmTBh9H3fx4/vevK45s6dm7XWWisTJ07M5ptvnlNPnZFddtk1W265Vc4//zPZYIMN
8qIXvWi5bXR1JV1dXaPm38f5PfaM1vO7qZxjAKPHaL+GjpiwXko5PckRSd5Ua/1jKeXxJNP6dZuY
1orxAzZt2prp6hpZYX3y5Kd1ugSG2eTJT8vUqWt2uoy26urqytpr/+24dt9915x22mnZd999s/vu
z84pp5yc8877dObPn5/nP//5+eIXv7DCf4OJE1dLklHz7+P8HntG4/ndZM4xgNFjtF9DR0RYL6V8
Nsm7kry11vqd3uY7kzyrX9f1k9y9MtueN+/RETeyvmDBY50ugWG2YMFjefDBRztdRltdffX1SfLk
cV1zzW+Xeb3nnq/Innu+YpnPrOjf4JhjTnzK90Yi5/fYMxrP7yZzjgGMHiP5GjqQXzI0PqyXUj6a
5LAkb661frvPW9cmObaUMrHWunQ6/AuTXLUy2+/u7kl3d097ih0mS5Z0d7oEhtmSJd1ZvNj3fSxw
fo89zu/h5RwDGD1G+zW00WG9lLJtkhOTfDLJ1aWUp/d5+xdJ7khySSllRpJ90rqX/aDhrhMAAADa
qel34++TVo0nprXy+11pTXO/q9banWTftKa+X5/kgCT71lr/0qFaAQAAoC0aPbJeaz09yel/5/0/
J9lr+CoCAACAodf0kXUAAAAYc4R1AAAAaBhhHQAAABpGWAcAAICGEdYBAACgYYR1AAAAaBhhHQAA
ABqm0c9ZB5LuJYtT602dLoNh4nsNAEAirEPjPfzgvfn6zGuyzv3rdroUhsEdM2/NwXl6p8sAAKDD
hHUYAdbZaN2st4UANxY8dNfc5K5OVwEAQKe5Zx0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0A
AAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAa
RlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgH
AACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACA
hhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHW
AQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAA
oGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGE
dQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAA
AGgYYR0AAAAaRlgHAACAhhHWAQAAoGGEdQAAAGgYYR0AAAAaRlgHAACAhhHWAQAAoGEmdLqAVVVK
mZjkgiRvTPLXJJ+qtZ7d2aoAAABg8EbDyPpZSXZJsmeS9yb5aCnljR2tCAAAAFbBiA7rpZRJSf41
yRG11v+utX43yRlJ3tfZygAAAGDwRnRYT7JjWlP5r+nT9ssku3WmHAAAAFh1Iz2sb5DkgVrr4j5t
9yZZo5SybodqAgAAgFUy0heYm5RkYb+2pa8nDmQD48Z1Zdy4rrYWNdTGjx+X+XPv7HQZDJNHIyz5
3QAACWhJREFU5t+XCXc+0ukyGCYP3zc/c+Y/1ukyGCZz5j+Y7cePy4QJI/135yOHa+jY4ho6triG
ji1j4Rra1dPT0+kaBq2U8i9Jzq21btinbZsks5KsW2t9qGPFAQAAwCCN9F9D3JlkvVJK3+NYP8lj
gjoAAAAj1UgP6zOTPJHkeX3aXpTkN50pBwAAAFbdiJ4GnySllAuTvCDJO5NsnOSSJAfVWr/TyboA
AABgsEb6AnNJ8oEkFyT5aZL5ST4iqAMAADCSjfiRdQAAABhtRvo96wAAADDqCOsAAADQMMI6AAAA
NIywDgAAAA0jrAMAAEDDCOvAiFJKmV1KObDTdQBAu5VS9iml3FFKeaSU8vJh2udmpZTuUsqmw7E/
YOCEdQAAaIZTklyRZJskVw7jfj3LGRpoQqcLAAAAkiRTkvyq1vqXThcCdJ6wDgy5UspmSWYneW2S
85Osl+R/J/lCkkuSbJvkZ0nekmRRktOTvCnJPye5M8kna61feIptfyTJu5NMSmsU4n211juG8HAA
oO1KKbOTbJrk4lLKR5PskeSCJC9Ncm9a18sZtdaeUso7khyU5EdJPpTk8STHJHksyaeSTE7y+Vrr
cb3b3jDJuUlektb1claSw2utV6+gjilJzkuyT5KHk/zfJMfUWh8fkgMHnpJp8MBwOi7J65L8a5Ij
0voB4NgkL0+ye5JDknw4yd5J3pBk67R+ODmvlPJP/TdWSjk8yf5phfzd0vph5vullPFDfSAA0GbP
TusX1EckeU5a18i7k+yYVjA/IMnxffrvnmSL3s/9Z5LP9X72tUk+mOSYUsqOvX2/kqQryfOS7JTk
jrR+EbAiX0qyVu/29+3d/mfbcHzAShLWgeF0Sq31xlrrN5Lcl+Rrtdaf1lqvSfLjtO7Rm5nkX2ut
v6m13pbktCSrpRXc+zs6ydG11qtqrTcneU9ao/avGoZjAYC2qbXOTbIkyYK0AvqmSd5da72l1npl
WiPo7+/zka60RsdvTfL5tEbMT+q9zl6c1nV2m96+3+7te3Ot9aYkFyaZ3r+GUsqWSV6f5MBa6x9r
rdcneVeSg0spa7f/qIG/xzR4YLj0pDUVfqnHkszp93pirfV7pZSXl1LOSuuHjF16P7vMaHkpZc0k
Gyf5eiml78I4a6QV7C9v/yEAwLDYNq1fPi8opSxtG5dkYillau/re/tMTX8srWvlctfV3q8/l+Qt
pZTnp3Vt3TUrHrTbtrf9rj77XWqrJL8f7AEBK09YB4bT4n6vu/t3KKXMSHJoWtPwvpzWaPmc/v3y
t/9//UuSm/u9N2/VygSAjpqQ5E9p3Tfe1e+9+b1/97+mJiu+rnalNXttcpKvJ/leWiH+W0+x34fS
CvP993vnAGsH2sQ0eKBJutJaLO7faq3H11q/mWTtPu89qdY6P60pfhvUWm/tnQZ4R5Izkyw3HAAA
I0hNaxr8A32ucc9I8rGs/GPWnpXkRUleWms9rdZ6RZIN/85+pyRJn/2umeSs/G2UHhgmRtaB4dL/
N/RP5YEk+5RSfpdkoySfTusHkxX9kHB2kk+WUu5P6weMjyR5fpKbVr1cAOiYH6Y1q+yrpZTjk0xN
clGSH/auBr+izzzVdfahtO6FP6CU8r0kz01ycpKUUlbv+9la602llB8k+VrvIq7dad0P/0CtdUE7
DgwYOCPrwHDpPxKwopGBniTvTGul2hvTmgr/9STXJdl5BZ87K63Hv12U5HdJNknyit5RdwAYaXqS
pNbanb9Ngb82yTeTXJbkyH/02RVs6860bik7Jq1r67FJDk9rGv2Krq1vS3JrWlPnf5jWdPz9B3tA
wOB19fSs7EwaAAAAYCgZWQcAAICGEdYBAACgYYR1AAAAaBhhHQAAABpGWAcAAICGEdYBAACgYYR1
AAAAaBhhHQAAABpGWAcAAICGmdDpAgCAoVVKOSjJO5JMTzI5yR1JLktyWq313iHc72ZJZifZs9Z6
5VDtBwBGIyPrADBKlVK6SinfSXJWku8meXGSrZK8L8lzklxfSllviMvoGeLtA8CoZGQdAEavDyTZ
O8lza63/3af9L6WUXyS5McmHkhw3hDV0DeG2AWDUEtYBYPR6X5JL+wX1JEmt9fFSyl5J7kmSUsqG
Sc5O8soki5NcneSDtdZbet+/uPejDyQ5MMlaSX6a5NBa69JtTE9ybpLdktyV5LT0G1kvpRyc5Ogk
m6c1Rf6iJJ+ttfb0mTZ/fJKjkjySZKda6yPt+McAgJHENHgAGIVKKVsk2SzJT56qT631jlrrE6WU
SUl+nmRJkhelNV3+/iS/LqVs0Ocj+yeZ2tvnVUl2TfLx3v1N7t3Xg0meneQ9ST7Sr6bDkpyR5KNJ
npXkxCTHJjm1X2kH9tbwJkEdgLHKyDoAjE5P7/37/r6NpZTvJdmrT9OctEbUpyR5e621u7f9kFLK
S5IcmuRjvW0PJXlXrXVJkptLKV9PK7QnrSA/KclBvQH7plLKUUn+b599nZhkRq31m72vbyulTEly
QSnlpD79zq+11kEdNQCMEsI6AIxOD/T+Pa1f+2FpheokOTLJ65LskmTdJPNLKX37TkyyTZ/Xf+4N
6ks9lGT13q+3S3Jzv5Hwq9N7z3rvQnYbJzm1lPKJPn3G9W5jiySP97bdMoDjA4BRTVgHgNHp1iR3
J9kzydKR7Cy9vzxJSinzer/sSnJTWsG9/4JwfcP3whXsp+spvk6SJ/p8vfTWu6Oy4qn5tyfZqPfr
x1bwPgCMKe5ZB4BRqHc6+7lJ3lFK2f4pum3a+/eNaS34Nr/Wemut9da0wvPpSfYY4C5/n6SUUvqO
5D8nvQvM1VrvS3Jfkmcs3Ufvfp6T5BOxajwALMPIOgCMXmck2SnJVaWU05NcnmR+kh3SWin+ZUn+
d5KvJvlwkm+VUo5NsiDJSWndj37iAPf1n0lOSPIfpZSj01qI7tMrqOfjpZQ7klyRZMckFyT5du9C
d4M9TgAYdYysA8AoVWvtqbXun+Rfk7wwyQ+S1CSfTXJvkj1qrYfVWhektcL7A0m+n+TXSTZI8rKB
LvRWa/1rWgvXLUryyyRfTuvRbX37nJ3Ws9//Lckfk5yT5HNprRy/1DKPegOAsaqrp8c1EQAAAJrE
yDoAAAA0jLAOAAAADSOsAwAAQMMI6wAAANAwwjoAAAA0jLAOAAAADSOsAwAAQMMI6wAAANAwwjoA
AAA0jLAOAAAADSOsAwAAQMP8f2O34sFEV03QAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The plot below gives a better picture of the same. While the deaths in the first and second class were contained, third class seems to be the worst affected for both men and women.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Builds a countplot split on travel class</span>
<span class="n">factorplt</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">factorplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s2">&quot;Sex&quot;</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s2">&quot;Survival&quot;</span><span class="p">,</span> <span class="n">col</span><span class="o">=</span><span class="s2">&quot;Pclass&quot;</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">titanic</span><span class="p">,</span> <span class="n">kind</span><span class="o">=</span><span class="s2">&quot;count&quot;</span><span class="p">)</span>

<span class="n">factorplt</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">ylabel</span> <span class="o">=</span> <span class="s2">&quot;Number of People&quot;</span><span class="p">,</span> <span class="n">xlabel</span> <span class="o">=</span> <span class="s2">&quot;Gender&quot;</span><span class="p">)</span>

<span class="n">titles</span> <span class="o">=</span> <span class="n">travelclass</span>

<span class="k">for</span> <span class="n">ax</span><span class="p">,</span> <span class="n">title</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">factorplt</span><span class="o">.</span><span class="n">axes</span><span class="o">.</span><span class="n">flat</span><span class="p">,</span> <span class="n">titles</span><span class="p">):</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="n">title</span><span class="p">)</span>
    
    <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">ax</span><span class="o">.</span><span class="n">patches</span><span class="p">:</span>
        <span class="n">height</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">get_height</span><span class="p">()</span>
        <span class="n">ax</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">get_x</span><span class="p">()</span><span class="o">+</span><span class="n">p</span><span class="o">.</span><span class="n">get_width</span><span class="p">()</span><span class="o">/</span><span class="mf">2.</span><span class="p">,</span>
                <span class="n">height</span> <span class="o">+</span> <span class="mi">3</span><span class="p">,</span>
                <span class="s1">&#39;{:1.2f}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">((</span><span class="n">height</span> <span class="o">*</span> <span class="mi">100</span><span class="p">)</span><span class="o">/</span><span class="n">totalpassengers</span><span class="p">),</span>
                <span class="n">ha</span><span class="o">=</span><span class="s2">&quot;center&quot;</span><span class="p">)</span> 

    
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
WQcnO2wAKmT9fhSwcKeznZ+Qdd+ZrJtvNwIeCILg/hx94rPWcQiQktX2QwH2T5KUP/O/JJU95n5J
2gWLk1L0LAZWAScDO85WsuMeMQBBEKzP+jUOWEDkYGXnm1jnPODYls924nbxO8D2HL/vuM3DLeQ/
3GQ50DDr9635LJckFYz5X5LKHnO/JO2C95yUoiRriMZ44MogCFruoluTrJ/ziNykemMYhovDMFxM
5IBhJNCpgJv8FgiCIMh5tvZYsm6KHYbhGmANcNiObWRt51jgfpzZT5IKhflfksoec78k7ZpXTkrR
9RDQBvgoCIKRwDvARqAVkdn8TgeeBl4CBgFvBEEwENgEDCVyT5m7CritV4E7gVeCILidyM2zx+UT
z31BEPwITAdaA48Cb2XdnHtf91OSlJv5X5LKHnO/JOXDKyelKArDMDMMw0uBa4AOwHtACEwAVgOd
wjC8NgzDTURm4VsH/BP4HKgPnF7Qm1OHYfgbkZttpwIfA88BD+7UZyzQD7gR+A54GHicyOx+O2Tu
085KkrKZ/yWp7DH3S1L+4jIzzTWSJEmSJEmSip9XTkqSJEmSJEmKCouTkiRJkiRJkqLC4qQkSZIk
SZKkqLA4KUmSJEmSJCkqLE5KkiRJkiRJigqLk5IkSZIkSZKiwuKkJEmSJEmSpKiwOClJkiRJkiQp
KixOSpIkSZIkSYoKi5OSJEmSJEmSosLipCRJkiRJkqSo+H/YHMV/YOdMUQAAAABJRU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The travel class has had a huge impact on the survival of passengers on the Titanic, with people travelling by 1st and 2nd class having a higher probability of survival and within those classes, women having a better chance of surviving over men.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="How-has-the-age-of-passengers-affected-the-survival-rate?">How has the age of passengers affected the survival rate?<a class="anchor-link" href="#How-has-the-age-of-passengers-affected-the-survival-rate?">&#182;</a></h3><p>There are a lot of instances where Age is either missing values or have fractionals in them. For this particular analysis, missing ages have been filled with 0 and the fractinals have been rounded.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">titanic</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">unique</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[11]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>array([ 22.  ,  38.  ,  26.  ,  35.  ,    nan,  54.  ,   2.  ,  27.  ,
        14.  ,   4.  ,  58.  ,  20.  ,  39.  ,  55.  ,  31.  ,  34.  ,
        15.  ,  28.  ,   8.  ,  19.  ,  40.  ,  66.  ,  42.  ,  21.  ,
        18.  ,   3.  ,   7.  ,  49.  ,  29.  ,  65.  ,  28.5 ,   5.  ,
        11.  ,  45.  ,  17.  ,  32.  ,  16.  ,  25.  ,   0.83,  30.  ,
        33.  ,  23.  ,  24.  ,  46.  ,  59.  ,  71.  ,  37.  ,  47.  ,
        14.5 ,  70.5 ,  32.5 ,  12.  ,   9.  ,  36.5 ,  51.  ,  55.5 ,
        40.5 ,  44.  ,   1.  ,  61.  ,  56.  ,  50.  ,  36.  ,  45.5 ,
        20.5 ,  62.  ,  41.  ,  52.  ,  63.  ,  23.5 ,   0.92,  43.  ,
        60.  ,  10.  ,  64.  ,  13.  ,  48.  ,   0.75,  53.  ,  57.  ,
        80.  ,  70.  ,  24.5 ,   6.  ,   0.67,  30.5 ,   0.42,  34.5 ,  74.  ])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">titanic</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">isnull</span><span class="p">()</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[12]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>177</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1"># A function to clean up the age field</span>
<span class="k">def</span> <span class="nf">cleanup</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">field</span><span class="p">,</span> <span class="n">convtoint</span><span class="p">):</span>
    
    <span class="c1">#Check if there are any missing values (Nan and make them 0</span>
    <span class="n">df</span><span class="p">[</span><span class="n">field</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">value</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="n">inplace</span> <span class="o">=</span> <span class="bp">True</span><span class="p">)</span>
    
    <span class="c1">#Check if it needs to be converted to int</span>
    <span class="k">if</span> <span class="n">convtoint</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
        <span class="n">df</span><span class="p">[</span><span class="n">field</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="n">field</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
    
    <span class="c1">#Round the values</span>
    <span class="n">df</span><span class="p">[</span><span class="n">field</span><span class="p">]</span><span class="o">.</span><span class="n">round</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
        
    <span class="k">return</span> <span class="n">field</span> <span class="o">+</span> <span class="s2">&quot; has been cleaned up&quot;</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">cleanup</span><span class="p">(</span><span class="n">titanic</span><span class="p">,</span> <span class="s2">&quot;Age&quot;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[14]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&#39;Age has been cleaned up&#39;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">average_age_titanic</span>    <span class="o">=</span><span class="n">titanic</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
<span class="n">std_age_titanic</span>        <span class="o">=</span><span class="n">titanic</span><span class="p">[</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">std</span><span class="p">()</span>

<span class="k">print</span> <span class="n">average_age_titanic</span>
<span class="k">print</span> <span class="n">std_age_titanic</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>23.7833894501
17.5973438421
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In the initial phase of analysis, filling the missing ages with 0, skewed the distribution graphs to the left and since 0 is not a valid age for those passengers and is just missing, Age 0 has been excluded from the analysis.</p>
<p>Although age 0 has been excluded for the purposes of this analysis, predictions or standardizing ages of those passengers could also be made to improve the accuracy of the charts.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">average_age_titanic</span>    <span class="o">=</span><span class="n">titanic</span><span class="p">[</span><span class="n">titanic</span><span class="o">.</span><span class="n">Age</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">][</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
<span class="n">std_age_titanic</span>        <span class="o">=</span><span class="n">titanic</span><span class="p">[</span><span class="n">titanic</span><span class="o">.</span><span class="n">Age</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">][</span><span class="s1">&#39;Age&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">std</span><span class="p">()</span>

<span class="k">print</span> <span class="n">average_age_titanic</span>
<span class="k">print</span> <span class="n">std_age_titanic</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>29.973125884
14.3032955152
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Builds a age distribution plot</span>
<span class="n">agedist</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">distplot</span><span class="p">(</span><span class="n">titanic</span><span class="p">[</span><span class="n">titanic</span><span class="o">.</span><span class="n">Age</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">][</span><span class="s1">&#39;Age&#39;</span><span class="p">])</span>
<span class="n">agedist</span><span class="o">.</span><span class="n">set_xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">max</span><span class="p">(</span><span class="n">titanic</span><span class="p">[</span><span class="n">titanic</span><span class="o">.</span><span class="n">Age</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">][</span><span class="s1">&#39;Age&#39;</span><span class="p">])</span><span class="o">+</span><span class="mi">10</span><span class="p">)</span>
<span class="n">agedist</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;Age distribution&quot;</span><span class="p">)</span>
<span class="n">agedist</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s2">&quot;Age&quot;</span><span class="p">)</span>
<span class="n">agedist</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s2">&quot;Density of population&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[17]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.text.Text at 0x937f610&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
IiIiIiKz3P8HYYMWtDD1+3oAAAAASUVORK5CYII=
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Builds a plot on age and survival</span>
<span class="n">ageplt</span> <span class="o">=</span> <span class="n">titanic</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;Survival&#39;</span><span class="p">,</span> <span class="s1">&#39;Age&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">.</span><span class="n">unstack</span><span class="p">(</span><span class="s1">&#39;Survival&#39;</span><span class="p">)[</span><span class="s2">&quot;PassengerId&quot;</span><span class="p">]</span>
<span class="n">ageplt</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;bar&#39;</span><span class="p">,</span> <span class="n">stacked</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">title</span> <span class="o">=</span> <span class="s2">&quot;Number of passengers over Age&quot;</span><span class="p">)</span>
<span class="n">pyplt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;Number of passengers&quot;</span><span class="p">)</span>
<span class="n">pyplt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;Age&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[18]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.text.Text at 0x94e0210&gt;</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
WtReITMhlyRJkqRVRHn5FH52xV2s3X2DNu/rizn/47LTYeDAbVtcd4011qRbtzIAevbswVlnncV7
733AhAlXcOutt+c61FWWCbkkSZIkrULW7r4BX+u1adphtNh++x3ID394PO+9N5t11vkaV155KU89
NZk11liTXXbZjZNP/hGdO3cG4KmnJnHTTX/gv/+dSUlJCYMH78A55/yCLl26AHDPPf/gj3+8mQUL
5nPood9Pc1it4qZukiRJkqQ2t/HGm1BTU8O7787kkkvOZ+HChfzudzdz8cW/Yvr0N/jNby4H4L33
ZvOLX5zDQQd9j4cffphf/vIyXn75Re677y4Ann/+WSZMuIITTzyV3/3uZqZPn7bsnvVVjTPkkiRJ
kqQ2t9ZaawHwzjtv8+9/T+Khh55gjTXWBOCss87lmGMO57TTfkpNTQ0//enP2Gef/enWbU26dl2H
bbcdxMyZ7wDwwAP3sscee7H77nsCMHr0WA444NvpDKqVTMglSZIkSW1uwYIFAPTrtynV1dXst99e
Dc6ZPXsWm222OZ06deKWW25k9uz/Mn16ZObMd9hjjyTpfvfdd9h//1HL6pSWrsP66/fOzyByzIRc
kiRJktTm3nrrTYqKipg9exZrrbU2N974R2pqapY7Z911e/DWW29yyinHs/POuzBkyGBGjTqEv/zl
z/VaW75ep06d2jj6tuE95JIkSZKkNvfAA/cSwuZsv/0Q5s//AoDevfvQu3cfFi9ezDXXXMWSJZU8
+uhDbL31Npx33oUccsghbL75N5k163/L2tlkk3688ca0Za8XLlzA7Nmz8z6eXHCGXJIkSZKUUwsW
zGfu3DnU1NQwf34FjzzyAI8//hhXXnktG2ywEYMHD2H8+DH89KdnUVRUzGWX/ZJ11vkaa665FqWl
6zBjxltMm1bO+uuvy623/onp06fRu3cfAA488GB++tNT2GqrgWy11dbceOP1fPnl4pRHnB0TckmS
JElahXwx538rPyln/WyXVd0JE65gwoQrAOjWrYwtt+zPNdf8ni22GADA2LEXcOWVl/OTn/yQDh06
sP32O/DjH58FwEEHHcLbb0d+9KOT6dKlC1ttNZAf/OB4Hn/8UQC22mprzj13LNdffy1XX/0Ze++9
L5tuGlo/4BSYkEuSJEnSKqJ//wFcdnrD8g4diikt7UpFxSKqqqqb1dbK62xH//4DWhzj3/9+33Kv
O3Ysplu3NZk3bwFLlyb9lJauw7hxFzZav0uXLowff3GDesccc8Kyc0aM2IMRI/ZocWztjQm5JEmS
JK0iSkpKGDhw2wbljSW9K5NNHeWWm7pJkiRJkpQCE3JJkiRJklJgQi5JkiRJUgpMyCVJkiRJSoEJ
uSRJkiRJKTAhlyRJkiQpBT72TJJWEZWVlZSXTwEaf25o//4DKCkpSTNESZIktYAJuSStIsrLpzDm
7vGU9i1rcKxi1lwuZFyjzyWVJElS+2RCLkmrkNK+ZZT165F2GJIkSU1aunQpt956I4888k8+/fQT
ysq6s9dee/L97x9LSUmXnPZ1003X89prrzBhwu9y2i7A0KGDuPrq37P11tvkvO1aJuSSJEmStIqo
ewtbXY3dzrYyzamTzS1x1103gZdeepFzzvkF66/fh48+eo+rrvo1b701g0suuaJFba3MYYcdyUEH
HZrTNvPJhFySJEmSVhEruoUt17K9Je6hhx7k3HPHss022wHQp8/6nHfeeRxxxBHMnTuHsrLuOYux
S5cudOmS21n3fHKXdUmSJElahdTewtbWX9km/cXFRbz88kvU1NQsK9tmm234y1/+TmnpOhx00L48
9NADy469+urLDB06CIAPP/yAoUMHccstN7D77rsyevRodtllCK+99sqy8xcuXMiwYTsyderr3HTT
9fzoRydRU1PD/vvvxT//+VW7AAce+B0ee+xhAP7zn1c57rgjGT58R4466lAmTXpiuXNvvPF69tln
d/beeyQPPHBvVmNvKWfIJUmSJEk5M2rUIdx44++ZPPlJhgzZicGDB7PnniPYaKONWbq08aXxRUVF
y72eOvV1brnlL6y9dmfmzJnHxIlPLLuX++mnJ1NWVsaWW/4fL7zw3LL6u+02gieffJzDDz94WRsV
FZ8zdOiuzJnzKWef/VNOPPFUvvWt7Skvn8JFF42nW7cyttlmG+644w7+9re/MmbMeNZdtwe//vXF
DWJqC+1ihjyE0C+E8HAI4YsQwrshhDPrHNsohPBYCGF+CGFqCGFkmrFKkiRJkpp29NHHMXbsBfTs
2Yv777+bc8/9GUOHDuXBB+9vdhsHH3wY66+/PhtssAEjRuzO5MlPLjs2adITDBs2okGd4cN354UX
nmfhwoUATJz4BEOG7ESXLl24++472W67wRxwwCh69+7D7rvvxT77HMDf/nY7AH//+9859NDDGTJk
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
Bwj3pv+EatgYAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>From the above visualization, it can be noted that the highest population of passengers is of the age group 16-40 and the least survival rate of passengers is of the age group 18-30.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="What-effect-did-the-fare-paid-have-on-survival-rate?">What effect did the fare paid have on survival rate?<a class="anchor-link" href="#What-effect-did-the-fare-paid-have-on-survival-rate?">&#182;</a></h3><p>As it is very noticeable from the Y-axis of the visualizations below, 1st class had fares upto a little more than 500 and it looks like only 2 passengers paid more than 500. What is interesting though is that a big majority of passengers in 1st class have paid less than 100 and on an verage people who have paid more have survived.</p>
<p>While in second and third classes, majority of passengers have paid fares below 30 and 20 respectively.</p>
<p>On an average, older people have paid lesser fares in all the classes alike and the chances of survival also decreases as the age of passenger increases.</p>
<p>Please note that the visualizations do not include passengers is age has missing values or is 0.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Builds a linear relationship between age and fare over survival </span>
<span class="n">fareplt</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">lmplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s2">&quot;Age&quot;</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s2">&quot;Fare&quot;</span><span class="p">,</span> <span class="n">hue</span> <span class="o">=</span> <span class="s1">&#39;Survival&#39;</span><span class="p">,</span> <span class="n">col</span><span class="o">=</span><span class="s2">&quot;Pclass&quot;</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">titanic</span><span class="p">[</span><span class="n">titanic</span><span class="o">.</span><span class="n">Age</span><span class="o">&gt;</span><span class="mi">0</span><span class="p">],</span> <span class="n">sharey</span> <span class="o">=</span> <span class="bp">False</span><span class="p">)</span>
<span class="n">fareplt</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">ylabel</span> <span class="o">=</span> <span class="s2">&quot;Fare&quot;</span><span class="p">,</span> <span class="n">xlabel</span> <span class="o">=</span> <span class="s2">&quot;Age&quot;</span><span class="p">)</span>
<span class="n">fareplt</span><span class="o">.</span><span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">(</span><span class="mi">0</span><span class="p">,)</span>
<span class="n">fareplt</span><span class="o">.</span><span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">(</span><span class="mi">0</span><span class="p">,)</span>
<span class="n">fareplt</span><span class="o">.</span><span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">(</span><span class="mi">0</span><span class="p">,)</span>
<span class="n">fareplt</span><span class="o">.</span><span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">,)</span>
<span class="n">fareplt</span><span class="o">.</span><span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">,)</span>
<span class="n">fareplt</span><span class="o">.</span><span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">,)</span>
<span class="n">titles</span> <span class="o">=</span> <span class="n">travelclass</span>

<span class="k">for</span> <span class="n">ax</span><span class="p">,</span> <span class="n">title</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">fareplt</span><span class="o">.</span><span class="n">axes</span><span class="o">.</span><span class="n">flat</span><span class="p">,</span> <span class="n">titles</span><span class="p">):</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="n">title</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
nf+zHXiDc+4H/vVp4FngH51zW8zsTiDrnLum7e9u8H/vSufcPUvZJxERkShRFouIiARPeSwisvQS
QRcgIpH028AI8JW2tr8Ffgd4K1AGWsDPZ690zlXN7Bdtt78AON3M5k+hbQGbAB20iYiIvDxlsYiI
SPCUxyIiS0wDGiJyNK7DO7j6hpnF/LaW//MHwCf9tkMtaxcHvgz8dyA277p9x61SERGR5ek6lMUi
IiJBuw7lsYjIktIeGiKyKGa2Eu8slC8A5wHn+j/nAXfgrQn6rH/zS9p+Lwlc2PanHgXOdM7tcM49
65x7FkgBfw6sP9H9EBERiSplsYiISPCUxyIiwdAMDRFZrN8DuoAbnXNPt19hZh/HO0PlfXhTbj9j
Zu8DRoEb8NYPnd2452bgHjO7DbgNGAQ+A6SBp058N0RERCJLWSwiIhI85bGISAA0Q0NEFus64Pvz
D9gA/DNJ7gbejXfgdi9wF/BTYBq4H6j5t70fuArvDJYH/d97Ani9c65+wnshIiISXdehLBYREQna
dSiPRUSWXKzVah3+ViIii2BmKeBq4AfOuWJb+5PA/3HOfSyw4kRERDqAslhERCR4ymMRkeNPAxoi
ckKY2QvAP+FtbNYArgc+CJznnNO0WRERkRNMWSwiIhI85bGIyPGlJadE5ER5I7AS+BnetNlL8KbM
6oBNRERkaSiLRUREgqc8FhE5jjRDQ0REREREREREREREQk8zNEREREREREREREREJPQ0oCEiIiIi
IiIiIiIiIqGnAQ0REREREREREREREQk9DWiIiIiIiIiIiIiIiEjoaUBDRERERERERERERERCTwMa
IiIiIiIiIiIiIiISehrQEBERERERERERERGR0NOAhoiIiIiIiIiIiIiIhJ4GNERERERERERERERE
JPT+PzIo1P8ck9//AAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="What-role-has-the-port-of-embarakation-played?">What role has the port of embarakation played?<a class="anchor-link" href="#What-role-has-the-port-of-embarakation-played?">&#182;</a></h3><p>While Southampton had the most number of passengers, it also had the least survival rate. This is probably because Southampton also had the most number of passengers in 3rd class. It can be concluded that Southampton is a really busy port.
Queenstown probably is the least popular port with minimal passengers, especially among 1st and 2nd travel classes.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">emb</span> <span class="o">=</span> <span class="n">titanic</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;Survival&#39;</span><span class="p">,</span> <span class="s1">&#39;Ports&#39;</span><span class="p">,</span><span class="s1">&#39;TravelClass&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">.</span><span class="n">unstack</span><span class="p">(</span><span class="s1">&#39;Ports&#39;</span><span class="p">)[</span><span class="s1">&#39;PassengerId&#39;</span><span class="p">]</span>
<span class="n">emb</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">6</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[20]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Ports</th>
      <th>Cherbourg</th>
      <th>Queenstown</th>
      <th>Southampton</th>
    </tr>
    <tr>
      <th>Survival</th>
      <th>TravelClass</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">Dead</th>
      <th>First Class</th>
      <td>26</td>
      <td>1</td>
      <td>53</td>
    </tr>
    <tr>
      <th>Second Class</th>
      <td>8</td>
      <td>1</td>
      <td>88</td>
    </tr>
    <tr>
      <th>Third Class</th>
      <td>41</td>
      <td>45</td>
      <td>286</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Survived</th>
      <th>First Class</th>
      <td>59</td>
      <td>1</td>
      <td>74</td>
    </tr>
    <tr>
      <th>Second Class</th>
      <td>9</td>
      <td>2</td>
      <td>76</td>
    </tr>
    <tr>
      <th>Third Class</th>
      <td>25</td>
      <td>27</td>
      <td>67</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Builds a bar plot betwen embarkation port and passengers survived over travel class</span>
<span class="n">portplt</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">barplot</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="s2">&quot;Ports&quot;</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="s2">&quot;Survived&quot;</span><span class="p">,</span> <span class="n">hue</span> <span class="o">=</span> <span class="s2">&quot;TravelClass&quot;</span><span class="p">,</span> <span class="n">hue_order</span> <span class="o">=</span> <span class="n">travelclass</span><span class="p">,</span> <span class="n">data</span> <span class="o">=</span> <span class="n">titanic</span><span class="p">,</span> <span class="n">estimator</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">,</span> <span class="n">ci</span> <span class="o">=</span> <span class="bp">None</span><span class="p">)</span>
<span class="n">portplt</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">ylabel</span> <span class="o">=</span> <span class="s2">&quot;People Survived&quot;</span><span class="p">,</span> <span class="n">xlabel</span> <span class="o">=</span> <span class="s2">&quot;Embarkation Area&quot;</span><span class="p">)</span>
<span class="n">portplt</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span> <span class="o">=</span> <span class="s2">&quot;Number of people that survived across travel class&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[21]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>[&lt;matplotlib.text.Text at 0xb221a50&gt;]</pre>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
RERERE5pRydP27LlL/r1683YsROoWfNCwHX9Tk+Ao6KiaNjwMubN+5K5c7/ilVcGA1C2bDlq176I
kSPfyLCv8PBiGWoKDQ2lfv1LmDdvDnXq/CPDuunTP+bDD99jypT/ZFgeH9+fc889j/j4YQQCAX7+
eQlz534FQGLieurXb8DNN9/G7t27mTjxTfr1682kSe+RmLieHj36AJCQ8CtxcV2oVSuW5s1b5MdJ
KxQ0hlxEREREROQ0ceDAfgKBAGFh4QB89903zJ37FYcPpxwpc8011zF58iSKFy+BMTUBaNToCtat
W8uXX35Gamoqa9as5rHHHmThwnlZ6mjf/v+YOfM/fPjh+xw4cICUlBTmz5/D+PFjefjhx7OU37dv
H2Fh4QQCATZv3sSbb44B4PDhwyxcOJ/evbuzY8d2SpQoQUREBNHRpQDo3bsbn3zybwDKli1LIBAg
Ojo6X8+X39RCLiIiIiIicoo43qPEqlU7hwceeJinnmpPamoq55xzLjfffCuLFy86UsaN1e7HLbfc
fmRZVFQUgwYNZ9iwQbz22itERkZy661tuO66G9NrPlK2Ro2aDB06hvHjx/LWW+NJSTlE1apnExfX
k6uuytjFHaBjx87Ex/dj6tQplC5dmptuuo3lyy1r167mjjvu4s8/N3D//W1JTk7CmFrExfUkNDSU
fv3iGT58MMOHD6F48eK0adOWBg0a/r0TWMgE0rsunK62bNlzeh/gGSA5OZmEhKV+h3HaiI2tQ1hY
mN9hiIiIiIictsqXL5mrh7CrhVwKvYSEpfT5oB+lKpf1O5RT3s4N2+h5Z3fq1bvY71BERERERM54
SsjllFCqclnKnVvB7zBERERERETyjSZ1ExEREREREfGBEnIRERERERERHyghFxEREREREfGBEnIR
ERERERERHyghFxEREREREfGBEnIRERERERERH+ixZyIiIiIiIrmUnJxMQsLSAq0zNrYOYWFhuS5/
++03sHnzpizLL7qoLqNGvUnHjo9Tv34DHnro0TzHsmLFcpKSDlK79kU5llm9ehWTJo1jyZLFHDx4
kOrVz+f++9vRqNHlACxZspinnmrPwoX/y3P9pxsl5CIiIiIiIrmUkLCUnkPfI7ps5QKpb9e2DfTp
BPXqXZzrbQKBAJ06daVZsxYZloeGFgWgf//XKFq06AnF063bs7Rr92iOCfnSpT/TpctTtGzZmkGD
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
IiIiIiIi4gMl5CIiIiIiIiI+UEIuIiIiIiIi4gMl5CIiIiIiIiI+UEIuIiIiIiIi4gMl5CIiIiIi
IiI+UEIuIiIiIiIi4gMl5CIiIiIiIiI+UEIuIiIiIiIi4gMl5CIiIiIiIiI+UEIuIiIiIiIi4oNQ
vwMAMMaEAUOAu4AkYIK1tru3rh4wBqgD/Ao8Ya390a9YRURERERERPJDYWkhHw40B1oAdwOPGmMe
NcZEAjOB+UB94DtgpjEmwrdIRURERERERPKB7y3kxpjSQDugmbV2sbfsNeBSIAXYb6193iveyRhz
LdAGeNuPeEVERERERETyQ2FoIb8C2Gmt/Tp9gbX2VWvtI8BlwNeZyn8DNCrA+ERERERERETyne8t
5MB5wBpjzH1ANyAMmAj0Ayrixo0H2wzEFmiEIiIiIiIiIvmsMCTkJYAawKPAg7gk/HVgHxCJm+Qt
WBIQXoDxiYiIiIiIiOS7wpCQpwAlgbuttYkAxpizgSeB5WRNvsOB/bndeUhIgJCQQD6FmntFihSG
0QAicrIUKRJCaKje5yIiIiJy4gpDQr4ROJiejHssUBWYC8RkKh/jbZMrZcoUJxAo+IQ8KkoTwYuc
zqKiIihdurjfYYiIiIjIKawwJOTfAcWMMedba1d6yy4EVgPfA3GZyjfGjS/Ple3b9/nSQr5794EC
r1NECs7u3QfYsWOf32GIiIiISCGU24Yb3xNya+0KY8xMYJIx5kncGPLngT7AVGCgMWYI8AbQHigO
TMnt/lNT00hNTcv/wI/j8OHUAq9TRArO4cOppKTofS4iIiIiJ66wDIC8B1gJLAQmASOstaOstXuA
64AmwCKgIdDaWqvmZxERERERETml+d5CDuAl3g96P5nXLQIuLuCQREQkk+TkZBISlvodxmkjNrYO
YWFhfochIiIiPioUCbmIiBR+CQlL6Tn0PaLLVvY7lFPerm0b6NMJ6tXT/WYREZEzmRJyERHJteiy
lSlbsbrfYYiIiIicFgrLGHIRERERERGRM4oSchEREREREREfKCEXERERERER8YESchEREREREREf
KCEXERERERER8YESchEREREREREfKCEXERERERER8YESchEREREREREfKCEXERERERER8YESchER
EREREREfKCEXERERERER8YESchEREREREREfKCEXERERERER8YESchEREREREREfKCEXERERERER
8YESchEREREREREfKCEXERERERER8YESchEREREREREfKCEXERERERER8YESchEREREREREfKCEX
ERERERER8YESchEREREREREfKCEXERERERER8YESchEREREREREfKCEXERERERER8YESchERERER
EREfKCEXERERERER8YESchEREREREREfKCEXERERERER8YESchEREREREREfKCEXERERERER8YES
chEREREREREfKCEXERERERER8YESchEREREREREfKCEXERERERER8YESchEREREREREfKCEXERER
ERER8YESchEREREREREfKCEXERERERER8YESchEREREREREfKCEXERERERER8YESchEREREREREf
KCEXERERERER8YESchEREREREREfhPodAIAx5mZgGpAGBLx/p1pr7zDG1APGAHWAX4EnrLU/+has
iIiIiIiISD4oLC3kFwLTgRjvpyLwiDEmEpgJzAfqA98BM40xEX4FKiIiIiIiIpIfCkULOVAL+NVa
uyV4oTGmHbDfWvu8t6iTMeZaoA3wdgHHKCIiIiIiIpJvClML+fJsll8KfJ1p2TdAo5MekYiIiIiI
iMhJVFhayA3QyhjTHSgCTAF64bqu/5qp7GYgtmDDExEREREREclfvifkxphqQARwANcV/VxgOBDp
/SRl2iQJCC/IGEVERERERETym+8JubV2nTGmrLV2p7foF2NMEeBfwFyyJt/hwP7c7j8kJEBISCB/
gs2DIkUKy2gAETkZihQJITT0zHqf63Mtf52J15CIiIhk5HtCDhCUjKf7HSgGbMLNuh4sBtiY232X
KVOcQKDgE/KoKE0EL3I6i4qKoHTp4n6HUaD0uZa/zsRrSERERDLyPSE3xrQE3gWqWGsPeovrAVuB
hUBcpk0aA/1yu//t2/f50kK+e/eBAq9TRArO7t0H2LFjn99hFCh9ruWvM/EaEhEROVPk9qa77wk5
8C2uC/o4Y0wfoDrwKjAQmAoMNMYMAd4A2gPFcZO+5UpqahqpqWn5HvTxHD6cWuB1ikjBOXw4lZSU
M+t9rs+1/HUmXkMiIiKSke+D16y1e4FrgPLA/4A3gbHW2kHW2j3AdUATYBHQEGhtrVUzjYiIiIiI
iJzSctVC7s2EnivW2nV5DcJa+zsuKc9u3SLg4rzuU0RERERERKQwy22X9TVAbvt9FzmxUERERERE
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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="n">emb</span> <span class="o">=</span> <span class="n">titanic</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;Survival&#39;</span><span class="p">,</span> <span class="s1">&#39;Ports&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">.</span><span class="n">unstack</span><span class="p">(</span><span class="s1">&#39;Ports&#39;</span><span class="p">)[</span><span class="s1">&#39;PassengerId&#39;</span><span class="p">]</span>
<span class="n">emb</span> <span class="o">=</span> <span class="n">emb</span><span class="o">/</span><span class="n">emb</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span><span class="o">*</span><span class="mi">100</span>
<span class="n">emb</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[22]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Ports</th>
      <th>Cherbourg</th>
      <th>Queenstown</th>
      <th>Southampton</th>
    </tr>
    <tr>
      <th>Survival</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dead</th>
      <td>44.642857</td>
      <td>61.038961</td>
      <td>66.304348</td>
    </tr>
    <tr>
      <th>Survived</th>
      <td>55.357143</td>
      <td>38.961039</td>
      <td>33.695652</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#Builds a function that builds a pie plot on survival/death rate</span>
<span class="k">def</span> <span class="nf">plotpie</span><span class="p">(</span><span class="n">series</span><span class="p">):</span>
    
    <span class="n">i</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="nb">list</span><span class="p">(</span><span class="n">series</span><span class="p">):</span>
        <span class="n">pyplt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">4</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span>
        <span class="n">pyplt</span><span class="o">.</span><span class="n">pie</span><span class="p">(</span><span class="n">emb</span><span class="p">[</span><span class="n">c</span><span class="p">],</span> <span class="n">labels</span><span class="o">=</span><span class="n">survival</span><span class="p">,</span> <span class="n">colors</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;red&#39;</span><span class="p">,</span> <span class="s1">&#39;green&#39;</span><span class="p">],</span> <span class="n">autopct</span><span class="o">=</span><span class="s1">&#39;</span><span class="si">%1.1f%%</span><span class="s1">&#39;</span><span class="p">,</span> \
                  <span class="n">shadow</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">startangle</span><span class="o">=</span><span class="mi">90</span><span class="p">)</span>
        <span class="c1"># View the plot drop above</span>
        <span class="n">pyplt</span><span class="o">.</span><span class="n">axis</span><span class="p">(</span><span class="s1">&#39;equal&#39;</span><span class="p">)</span>
        <span class="n">pyplt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Survival Rate at &quot;</span> <span class="o">+</span> <span class="n">c</span><span class="p">)</span>

        
        <span class="n">i</span><span class="o">+=</span> <span class="mi">1</span>
        
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span></span><span class="c1">#To build pie plots at different embarkation ports</span>
<span class="n">plotpie</span><span class="p">(</span><span class="n">emb</span><span class="p">[[</span><span class="s2">&quot;Cherbourg&quot;</span><span class="p">,</span> <span class="s2">&quot;Queenstown&quot;</span><span class="p">,</span> <span class="s2">&quot;Southampton&quot;</span><span class="p">]])</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
wumOAAAAAElFTkSuQmCC
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Conclusion">Conclusion<a class="anchor-link" href="#Conclusion">&#182;</a></h3><p>The features below were analyzed in this analysis:</p>
<ul>
<li>Gender</li>
<li>Travel Class</li>
<li>Age</li>
<li>Fare</li>
<li>Port of Embarkation</li>
</ul>
<p>The most evident findings in this analysis are that:</p>
<ul>
<li>passengers in the upper class had a better chance of surviving than the passengers in lower class</li>
<li>women had a better chance of surviving over men</li>
<li>passengers with ages between 18 and 30 were more and also had a very poor survival rate</li>
<li>Southamptopn port seemed busier and popular with more number of passengers and Queenstown port the least with very few passengers especially in first and second classes</li>
</ul>
<h3 id="Limitations">Limitations<a class="anchor-link" href="#Limitations">&#182;</a></h3><p>Some limitations of this analysis include the dataset and the missing values in Age and Cabin. This dataset contains details about less than half the passengers on Titanic within which age and cabin have more than 170 and 650 missing values respectively.</p>
<p>Filling the missing values of age with 0 results in skewing the visualizations to the left and so, this analysis excludes the records with age missing or 0.</p>
<p>Cabin also could be a strong indicator of survival as some survival boats could have been more accessible from some of the cabin areas and some might have very little or late access.</p>
<p>The precision of this analysis could be improved with more information on these fields and with a larger dataset.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="References">References<a class="anchor-link" href="#References">&#182;</a></h3><ol>
<li><a href="https://www.kaggle.com/c/titanic">Kaggle</a></li>
<li><a href="http://seaborn.pydata.org/tutorial.html">Seaborn</a></li>
<li><a href="http://matplotlib.org/">Matplotlib</a></li>
<li><a href="http://pandas.pydata.org/">Pandas</a></li>
</ol>

</div>
</div>
</div>
    </div>
  </div>
</body>

 


</html>

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
