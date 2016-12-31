# -*- coding: latin-1 -*-
# - HTML Page Code

main_nav_html_basic = '''
<a href="/"><div>Main Page</div></a>
<a href="../../profiles"><div>Profiles</div></a>
<a href="../../blog"><div>Blog</div></a>
<a href="../../videos"><div>Videos</div></a>
'''

test_page_html = '''



hi hi .......... dth dth 


play around and get and idea


'''

manage_blog_page_html_admin = '''
hi test

'''




main_nav_html = '''
<a href="/"><div>Main Page</div></a>
<a href="../../profiles"><div>Profiles</div></a>
<a href="../../blog"><div>Blog</div></a>
<a href="../../videos"><div>Videos</div></a>

<style>
.aside_social_wrap { position: absolute; bottom: 0; font-size: 12px; width: 175px; margin: 0 auto; }
.aside_social_item_wrap { margin-bottom: 15px; }
.aside_social_item_wrap img { height: 16px; }
.aside_social_item_wrap a { color: #222; font-family: serif; }
</style>
  <div class="aside_social_wrap">
    <div class="aside_social_item_wrap">
      <a href="https://www.youtube.com/channel/UCtlEfo4PHGw1hkept5WAw1g" target="_blank">
        <img src="../../pics/logo_youtube.png" />
        <p>Watch YouTube Channel</p>
      </a>
    </div><!-- . aside_social_item_wrap - -->

    <div class="aside_social_item_wrap">
      <a href="https://www.facebook.com/DC2BeRev" target="_blank">
        <img src="../../pics/logo_facebook_1.png" /> &nbsp;
        <img src="../../pics/logo_facebook_2.png" />
        <p>Like Facebook Page</p>
      </a>
    </div><!-- . aside_social_item_wrap - -->

  </div><!-- . aside_social_wrap - -->

'''

footer_left_aside = '''
<style>
.footer_social_wrap { font-size: 12px; }
.footer_social_item_wrap { display: inline-block; margin-left: 25px; text-align: center; }
.footer_social_item_wrap img { height: 16px; }
.footer_social_item_wrap a { color: #222; font-family: serif; }
</style>
  <div class="footer_social_wrap">
    <div class="footer_social_item_wrap">
      <a href="https://www.youtube.com/channel/UCtlEfo4PHGw1hkept5WAw1g" target="_blank">
        <img src="../../pics/logo_youtube.png" />
        <p>YouTube</p>
      </a>
    </div><!-- . footer_social_item_wrap - -->

    <div class="footer_social_item_wrap">
      <a href="https://www.facebook.com/DC2BeRev" target="_blank">
        <img src="../../pics/logo_facebook_1.png" /> &nbsp;
        <img src="../../pics/logo_facebook_2.png" />
        <p>Facebook</p>
      </a>
    </div><!-- . footer_social_item_wrap - -->
  </div><!-- . footer_social_wrap - -->
'''


footer_right_aside = '''
<div class="footer_right_text">Live Your Dream</div>
<div class="footer_logo_wrap">
  <img src="../../pics/logo.jpg" />
</div><!-- . footer_logo_wrap - -->

'''




enter_page_html = '''
<style>
.enter_page_wrap { text-align: center; padding-top: 50px; }
.page_title { padding-bottom: 25px; }
.sign_in_message { margin-top: 25px; }
</style>
<div class="enter_page_wrap">
<div class="page_title">Live Your Dream</div>

<img src="../../pics/jumpgirl.jpg" />

  <div class="sign_in_message">
    Please Sign In
  </div><!-- . sign_in_message - -->
</div><!-- . enter_page_wrap - -->
'''


dashboard_page_html = '''
hi

'''



videos_page_html = '''<style>
.new_post_button_wrap { position: relative; margin-bottom: 25px; height: 30px; }
.new_post_button { position: absolute; right: 10px; width: 75px; border: 1px solid #ccc; padding: 10px; text-align: center; border-radius: 5px; font-size: 12px; color: #00796B; }
.new_post_button:hover { border: 1px solid #00796B; color: #222; }

.video_list_wrap { outline: 1px solid #eee; min-height: 175px; padding-top: 15px; padding-bottom: 25px; }
.video_list_data { }
.video_item_wrap { border: 1px solid #ccc; margin: 25px; padding: 15px; min-height: 75px; }
.video_item_data { position: relative; }

.post_date_wrap { font-size: 12px; position: absolute; right: 5px; text-align: right; }

</style>

<p>Videos</p>

<div class="new_post_button_wrap"><a href="../../publish/new_video">
  <div class="new_post_button">New Video</div></a>
</div><!-- . .new_post_button_wrap - -->

<div class="video_list_wrap">
  <div class="video_list_data">
    <div class="video_item_wrap" ng-repeat="item in video_page_data">
      <a href="../../video_id?[!item.data_id!]"><div class="video_item_data">
        hi [!item.video_id!] - [!item.data_id!]
      </div><!-- . video_item_data - --></a>
    </div><!-- . video_item_wrap - -->
  </div><!-- . video_list_data - -->
</div><!-- . video_list_wrap - -->

<script>

function googleApiClientReady() {

    var apiKey = 'your api key';

    gapi.client.setApiKey(apiKey);
    gapi.client.load('youtube', 'v3', function() {

        request = gapi.client.youtube.search.list({
            part: 'snippet',
            channelId: 'UCtlEfo4PHGw1hkept5WAw1g',
            order: 'date',
            type: 'video'

        });

        request.execute(function(response) {
                console.log(response);

        });
    });

}
  </script>
    <script src="https://apis.google.com/js/client.js?onload=googleApiClientReady"></script>


'''


create_new_video_page_html = '''
<style>

.publish_blog_form_wrap { width: 100%; margin: 0 auto; padding-bottom: 75px; }
.publish_blog_form_data { border: 25px solid #eee; padding: 50px; padding-top: 75px; min-height: 250px; }

form { outline: 1px solid #eee;  margin: 0 auto; padding: 25px; }

td.label { text-align: right; padding-right: 10px; font-size: 12px; width: 65px; }
td.input { }
input[type="text"] { width: 98%; height: 20px; }
textarea { width: 275px; height: 175px; }


</style>

<div class="publish_blog_form_wrap">
  <div class="publish_blog_form_data">
    <p class="page_title">Create New Video Page</p>
    <form action="../../add_new_video_post" method="post" enctype="multipart/form-data">
      <table>
        <tr>
          <td class="label">Video Name</td>
          <td class="input"><input type="text" name="video_name" /></td>
        </tr>
        <tr>
          <td class="label">Video About</td>
          <td class="input">
            <input type="text" name="video_about" />
          </td>
        </tr>
        <tr>
          <td></td>
          <td style="text-align:right;"><input type="submit" value="Next" /></td>
        </tr>
      </table>
      <input type="hidden" name="data_action" value='Add'>
    </form>
  </div><!-- . publish_blog_form_data - -->
</div><!-- . publish_blog_form_wrap - -->

'''


upload_new_video_data_html = '''

<div class="publish_blog_form_wrap">
  <div class="publish_blog_form_data">
    <p class="page_title">Upload New Video Data</p>
    <form action="{0}" method="post" enctype="multipart/form-data">
      <table>
        <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' required/></td>
          </tr>
        <tr>
          <td class="label">Video File</td>
          <td class="input">
            <input type="file" name="video_file" />
          </td>
        </tr>
        <tr>
          <td></td>
          <td style="text-align:right;"><input type="submit" value="Publish" /></td>
        </tr>
      </table>
      <input type="hidden" name="data_action" value='Add'>
    </form>
  </div><!-- . publish_blog_form_data - -->
</div><!-- . publish_blog_form_wrap - -->

'''



blog_post_page_html = '''<style>

.blog_post_head_data { position: relative; }
.post_date_wrap { position: absolute; right: 10px; top: 10px; }

.blog_post_text_wrap { font-family: sans-serif; }

</style>

<div class="blog_post_wrap">
  <div class="blog_post_data">
    <div class="blog_post_head_wrap">
      <div class="blog_post_head_data">
        <div class="post_date_wrap">
          [!blog_post_data.blog_post_date!]</p>
        </div><!-- . post_date_wrap - -->
        <div class="post_name_wrap">
          <p>[!blog_post_data.blog_post_name!]</p>
        </div><!-- . post_name_wrap - -->
      </div><!-- . blog_post_head_data - -->
    </div><!-- . blog_post_head_wrap - -->
    <div class="blog_post_body_wrap">

    </div><!-- . blog_post_body_wrap - -->
  </div><!-- . blog_post_data - -->
</div><!-- . blog_post_wrap - -->

'''


blog_page_html = '''<style>

.new_post_button_wrap { position: relative; margin-bottom: 25px; height: 30px; }
.new_post_button { position: absolute; right: 10px; width: 75px; border: 1px solid #ccc; padding: 10px; text-align: center; border-radius: 5px; font-size: 12px; color: #00796B; }
.new_post_button:hover { border: 1px solid #00796B; color: #222; }

.blog_list_wrap { outline: 1px solid #eee; min-height: 175px; padding-top: 15px; padding-bottom: 25px; }
.blog_list_data { }
.blog_item_wrap { border: 1px solid #ccc; margin: 25px; padding: 15px; min-height: 75px; }
.blog_item_data { position: relative; }

.post_date_wrap { font-size: 12px; position: absolute; right: 5px; text-align: right; }

.blog_post_author_wrap { float: left; }
.blog_post_author_icon { width: 75px; }
.blog_post_author_icon img { width: 100%; }


</style>

<div class="page_title">
  <p>Blog Page</p>
</div>

<div class="new_post_button_wrap"><a href="../../publish/blog_post">
  <div class="new_post_button">New Post</div></a>
</div><!-- . .new_post_button_wrap - -->

<div class="blog_list_wrap">
  <div class="blog_list_data">

    <div class="blog_item_wrap">
      <a href="../../blog_post_id?demo_post"><div class="blog_item_data">
        <div class="blog_post_author_wrap">
          <div class="blog_post_author_icon">
            <img src="../../pics/jumpgirl.jpg" />
          </div>
        </div><!-- . blog_post_author_wrap - -->
        <div class="post_date_wrap">post date</div>
         [!item.blog_post_name!] - [!item.data_id!]
      </div><!-- . blog_item_data - --></a>
    </div><!-- . blog_item_wrap - -->

    <div class="blog_item_wrap" ng-repeat="item in blog_page_data">
      <a href="../../blog_post_id?[!item.data_id!]"><div class="blog_item_data">
        <div class="post_date_wrap">[!item.blog_post_date!]<br />post date</div>
         [!item.blog_post_name!] 


      </div><!-- . blog_item_data - --></a>
    </div><!-- . blog_item_wrap - -->
  </div><!-- . blog_list_data - -->
</div><!-- . blog_list_wrap - -->

'''



publish_blog_post_html = '''
<script src="../../files/jquery-2.2.2.min.js" type="text/javascript" charset="utf-8"></script>

<script src="../../files/wysihtml.js"></script>
<script src="../../files/wysihtml.all-commands.js"></script>
<script src="../../files/wysihtml.table_editing.js"></script>
<script src="../../files/wysihtml.toolbar.js"></script>
  
<script src="../../files/advanced_and_extended.js"></script>
<style>

.publish_blog_form_wrap { width: 100%; margin: 0 auto; padding-bottom: 75px; }
.publish_blog_form_data { border: 25px solid #eee; padding: 50px; padding-top: 75px; min-height: 250px; }

form { outline: 1px solid #eee;  margin: 0 auto; padding: 25px; }

td.label { text-align: right; padding-right: 10px; font-size: 12px; width: 65px; }
td.input { }
input[type="text"] { width: 98%; height: 20px; }
textarea { width: 275px; height: 175px; }

h2 { margin-bottom: 0; }
small { display: block; margin-top: 40px; font-size: 9px; }
small, small a { color: #666; }
.toolbar a { color: #000; text-decoration: underline; cursor: pointer; }
#toolbar [data-wysihtml-action] { float: right; }
#toolbar, textarea { padding: 5px;
  -webkit-box-sizing: border-box;
  -ms-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box; }
textarea { width: 100%; height: 280px; border: 1px solid #bbb; font-family: Verdana; font-size: 11px; }
textarea:focus { color: black; border: 2px solid black; }
.wysihtml-command-active, .wysihtml-action-active { font-weight: bold; }
[data-wysihtml-dialog] { margin: 5px 0 0; padding: 5px; border: 1px solid #666; }
a[data-wysihtml-command-value="red"] { color: red; }
a[data-wysihtml-command-value="green"] { color: green; }
a[data-wysihtml-command-value="blue"] { color: blue; }
.wysihtml-editor, .wysihtml-editor table td { outline: 1px dotted #abc; }
code { background: #ddd; padding: 10px; white-space: pre; display: block;margin: 1em 0; }

.toolbar { display: block; border-radius: 3px; border: 1px solid #fff; margin-bottom: 9px; line-height: 1em; }
.toolbar a { display: inline-block; height: 1.5em; border-radius: 3px; font-size: 9px; line-height: 1.5em; text-decoration: none; background: #e1e1e1; border: 1px solid #ddd; padding: 0 0.2em; imargin: 1px 0; }
.toolbar a.wysihtml-command-active, .toolbar .wysihtml-action-active { background: #222; color: white; }
.toolbar .block { padding: 1px 1px; display: inline-block; background: #eee; border-radius: 3px; margin: 0px 1px 1px 0; }
div[data-wysihtml-dialog="createTable"] { position: absolute; background: white; }
div[data-wysihtml-dialog="createTable"] td { width: 10px; height: 5px; border: 1px solid #666; }
.wysihtml-editor table td.wysiwyg-tmp-selected-cell { outline: 2px solid green; }
.editor-container-tag { padding: 5px 10px; position: absolute; color: white; background: rgba(0,0,0,0.8); width: 100px; margin-left: -50px; -webkit-transition: 0.1s left, 0.1s top; }
.wrap { max-width: 700px; margin: 40px; }
.editable { min-height: 250px; padding: 10px; }
.editable .wysihtml-uneditable-container { outline: 1px dotted gray; position: relative; }
.editable .wysihtml-uneditable-container-right { float: right; width: 50%; margin-left: 2em; margin-bottom: 1em; }
.editable .wysihtml-uneditable-container-left { float: left; width: 50%; margin-right: 2em; margin-bottom: 1em; }
.wysiwyg-font-size-smaller { font-size: smaller; }
.wysiwyg-font-size-larger { font-size: larger; }
.wysiwyg-font-size-xx-large { font-size: xx-large; } 
.wysiwyg-font-size-x-large { font-size: x-large; }
.wysiwyg-font-size-large { font-size: large; }
.wysiwyg-font-size-medium { font-size: medium; }
.wysiwyg-font-size-small { font-size: small; }
.wysiwyg-font-size-x-small { font-size: x-small; }
.wysiwyg-font-size-xx-small { font-size: xx-small; }
.wysiwyg-color-black { color: black; }
.wysiwyg-color-silver { color: silver; }
.wysiwyg-color-gray { color: gray; }
.wysiwyg-color-white { color: white; }
.wysiwyg-color-maroon { color: maroon; }
.wysiwyg-color-red { color: red; }
.wysiwyg-color-purple { color: purple; }
.wysiwyg-color-fuchsia { color: fuchsia; }
.wysiwyg-color-green { color: green; }
.wysiwyg-color-lime { color: lime; }
.wysiwyg-color-olive { color: olive; }
.wysiwyg-color-yellow { color: yellow; }
.wysiwyg-color-navy { color: navy; }
.wysiwyg-color-blue { color: blue; }
.wysiwyg-color-teal { color: teal; }
.wysiwyg-color-aqua { color: aqua; }
.wysiwyg-text-align-right { text-align: right; }
.wysiwyg-text-align-center { text-align: center; }
.wysiwyg-text-align-left { text-align: left; }
.wysiwyg-text-align-justify { text-align: justify; }
.wysiwyg-float-left { float: left; margin: 0 8px 8px 0; }
.wysiwyg-float-right { float: right; margin: 0 0 8px 8px; }
.wysiwyg-clear-right { clear: right; }
.wysiwyg-clear-left { clear: left; }


</style>

<div class="publish_blog_form_wrap">
  <div class="publish_blog_form_data">
    <p class="page_title">Publish New Blog Post</p>
    <form action="../../add_student_blog_post" method="post">
      <table>
        <tr>
          <td class="label">Post Name</td>
          <td class="input"><input type="text" name="blog_post_name"></td>
        </tr>
        <tr>
          <td class="label">Post Text</td>
          <td class="input">
            <div class="ewrapper" contentEditable="false">
            <div class="toolbar" style="display: none;">
                <div class="block">
                  <a data-wysihtml-command="bold" title="CTRL+B">bold</a>
                  <a data-wysihtml-command="italic" title="CTRL+I">italic</a>
                  <a data-wysihtml-command="underline" title="CTRL+U">underline</a>
                  <a data-wysihtml-command="superscript" title="sup">superscript</a>
                  <a data-wysihtml-command="subscript" title="sub">subscript</a>
                </div>
                <div class="block">
                  <a data-wysihtml-command="createLink">link</a>
                  <a data-wysihtml-command="removeLink"><s>link</s></a>
                  <a data-wysihtml-command="insertImage">image</a>
                  <a data-wysihtml-command="formatBlock" data-wysihtml-command-value="h1">h1</a>
                  <a data-wysihtml-command="formatBlock" data-wysihtml-command-value="h2">h2</a>
                  <a data-wysihtml-command="formatBlock" data-wysihtml-command-value="h3">h3</a>
                  <a data-wysihtml-command="formatBlock" data-wysihtml-command-value="p">p</a>
                  <a data-wysihtml-command="formatBlock" data-wysihtml-command-value="pre">pre</a>
                  <a data-wysihtml-command="formatBlock" data-wysihtml-command-blank-value="true">plaintext</a>
                  <a data-wysihtml-command="insertBlockQuote">blockquote</a>
                  <a data-wysihtml-command="formatCode" data-wysihtml-command-value="language-html">Code</a>
                </div>
                
                <div class="block">
                  <a data-wysihtml-command="fontSizeStyle">Size</a>
                  <div data-wysihtml-dialog="fontSizeStyle" style="display: none;">
                    Size:
                    <input type="text" data-wysihtml-dialog-field="size" style="width: 60px;" value="" />
                    <a data-wysihtml-dialog-action="save">OK</a>&nbsp;<a data-wysihtml-dialog-action="cancel">Cancel</a>
                  </div>
                </div>
                
                <div class="block">
                  <a data-wysihtml-command="insertUnorderedList">&bull; List</a>
                  <a data-wysihtml-command="insertOrderedList">1. List</a>
                </div>
                <div class="block">
                  <a data-wysihtml-command="outdentList">&lt;-</a>
                  <a data-wysihtml-command="indentList">-&gt;</a>
                </div>
                <div class="block">
                  <a data-wysihtml-command="justifyLeft">justifyLeft</a>
                  <a data-wysihtml-command="justifyRight">justifyRight</a>
                  <a data-wysihtml-command="justifyFull">justifyFull</a>
                </div>

                <div class="block">
                  <a data-wysihtml-command="alignLeftStyle">alignLeft</a>
                  <a data-wysihtml-command="alignRightStyle">alignRight</a>
                  <a data-wysihtml-command="alignCenterStyle">alignCenter</a>
                </div>
              
                <div class="block">
                  <a data-wysihtml-command="foreColorStyle">Color</a>
                  <div data-wysihtml-dialog="foreColorStyle" style="display: none;">
                    Color:
                    <input type="text" data-wysihtml-dialog-field="color" value="rgba(0,0,0,1)" />
                    <a data-wysihtml-dialog-action="save">OK</a>&nbsp;<a data-wysihtml-dialog-action="cancel">Cancel</a>
                  </div>
                </div>
                
                <div class="block">
                  <a data-wysihtml-command="bgColorStyle">BG Color</a>
                  <div data-wysihtml-dialog="bgColorStyle" style="display: none;">
                    Color:
                    <input type="text" data-wysihtml-dialog-field="color" value="rgba(0,0,0,1)" />
                    <a data-wysihtml-dialog-action="save">OK</a>&nbsp;<a data-wysihtml-dialog-action="cancel">Cancel</a>
                  </div>
                </div>
                
                <div class="block">
                  <a data-wysihtml-command="undo">undo</a>
                  <a data-wysihtml-command="redo">redo</a>
                </div>
              
                <div class="block">
                  <a data-wysihtml-action="change_view">HTML</a>
                </div>
              
                <div data-wysihtml-dialog="createLink" style="display: none;">
                  <label>
                    Link:
                    <input data-wysihtml-dialog-field="href" value="http://">
                  </label>
                  <a data-wysihtml-dialog-action="save">OK</a>&nbsp;<a data-wysihtml-dialog-action="cancel">Cancel</a>
                </div>
                <div data-wysihtml-dialog="insertImage" style="display: none;">
                  <label>
                    Image:
                    <input data-wysihtml-dialog-field="src" value="http://">
                  </label>
                  <label>
                    Align:
                    <select data-wysihtml-dialog-field="className">
                      <option value="">default</option>
                      <option value="wysiwyg-float-left">left</option>
                      <option value="wysiwyg-float-right">right</option>
                    </select>
                  </label>
                  <a data-wysihtml-dialog-action="save">OK</a>&nbsp;<a data-wysihtml-dialog-action="cancel">Cancel</a>
                </div>
              </div><!-- toolbar -->

              <textarea class="editable" name="blog_post_text" data-placeholder=". . . type here">

              </textarea><!-- . editable - -->


            </div><!-- . ewrapper - -->
          </td>
        </tr>
        <tr>
          <td></td>
          <td style="text-align:right;"><input type="submit" value="Publish" /></td>
        </tr>
      </table>
      <input type="hidden" name="data_action" value='Add'>
    </form>
  </div><!-- . publish_blog_form_data - -->
</div><!-- . publish_blog_form_wrap - -->


<script>
var editors = [];

  $('.ewrapper').each(function(idx, wrapper) {
    var e = new wysihtml.Editor($(wrapper).find('.editable').get(0), {
      toolbar:        $(wrapper).find('.toolbar').get(0),
      parserRules:    wysihtmlParserRules,
      pasteParserRulesets: wysihtmlParserPasteRulesets
      //showToolbarAfterInit: false
    });
    editors.push(e);
    
    e.on("showSource", function() {
      alert(e.getValue(true));
    });
    
  });
  
</script>
'''





profiles_page_html = '''<style>

.profile_item_wrap { margin: 25px; }

.section_wrap { margin: 25px; }
.student_profile_list_wrap { margin: 25px; }
.doctor_profile_list_wrap { margin: 25px; }

.new_profile_section_wrap { text-align: center; }
.center_image_wrap { width: 150px; margin: 0 auto; }
.center_image_wrap img { width: 100%; }

.new_profile_button_wrap { display: inline-block; border: 1px solid #777; border-radius: 3px; margin: 25px; font-family: sans-serif; font-size: 12px; color: #000; }
.new_profile_button_wrap:hover { border: 1px solid #111; }
.new_profile_button_data { padding: 10px; }

@media (min-width: 500px) { 

.center_image_wrap { width: 200px; }

}
</style>

<p>Profiles Page</p>


<div class="new_profile_section_wrap">
  <div class="center_image_wrap">
    <img src="../../pics/jumpgirl.jpg" />
  </div><!-- . center_image_wrap - -->

  <p class="page_title">Create New Profile</p>

  <a href="../../profiles/new_student">
    <div class="new_profile_button_wrap">
      <div class="new_profile_button_data">
        For Student
    </div><!-- . new_profile_button_data - -->
  </div><!-- . new_profile_button_wrap - --></a>


  <a href="../../profiles/new_doctor">
  <div class="new_profile_button_wrap">
    <div class="new_profile_button_data">
      For Doctor
    </div><!-- . new_profile_button_data - -->
  </div><!-- . new_profile_button_wrap - --></a>


</div><!-- . new_profile_section_wrap - -->

  <div class="student_profile_list_wrap">
    <div class="student_profile_list_data">
      <div class="student_profile_item_wrap" ng-repeat="item in student_users_data">
        <a href="../../profile_id?student-[!item.data_id!]"><div class="blog_item_data">
          hi [!item.student_name!] - [!item.data_id!]
        </div><!-- . student_profile_item_data - --></a>
      </div><!-- . student_profile_item_wrap - -->
    </div><!-- . student_profile_list_data - -->
  </div><!-- . student_profile_list_wrap - -->

</div><!-- . section_wrap - -->

<div class="section_wrap">

  <div class="doctor_profile_list_wrap">
    <div class="doctor_profile_list_data">
      <div class="doctor_profile_item_wrap" ng-repeat="item in doctor_users_data">
        <a href="../../profile_id?doctor-[!item.data_id!]"><div class="blog_item_data">
          hi [!item.doctor_name!] - [!item.data_id!]
        </div><!-- . doctor_profile_item_data - --></a>
      </div><!-- . doctor_profile_item_wrap - -->
    </div><!-- . doctor_profile_list_data - -->
  </div><!-- . doctor_profile_list_wrap - -->

</div><!-- . section_wrap - -->

'''







#----------------------------------------------#
#            Student HTML Page Code            #
#----------------------------------------------#

student_nav_html = '''
<a href="../../new/profile"><div>Create New Profile</div></a>
<a href="../../view/profile"><div>View Student Profile</div></a><br />
<a href="../../new/post"><div>Write Blog Post</div></a>
<a href="../../new/video"><div>Upload Video</div></a>
<a href="../../new/audio"><div>Upload Audio</div></a>
<a href="newsletter"><div>Student Newsletter</div></a>

'''

student_profile_page_html = '''<style>

.student_header_wrap { padding: 25px; width:  90%; margin: 0 auto; outline: 1px solid #eee; margin-bottom: 45px; }
.student_header_photo { display: inline-block; margin: 25px; width: 250px; }
.student_header_photo img { width: 100%; }
.main_logo_wrap { display: inline-block; width: 225px; margin: 25px; }
.main_logo_wrap img { width: 100%; }

.main_body_wrap { min-height: 550px; }
.page_title { color: #00796B; }


.student_contact_info_wrap { border: 25px solid #FAFAFA; margin-top: 45px; margin-bottom: 50px; }
.student_contact_info_data { border: 1px solid #ccc; padding: 10px; }
.head_name { display: inline-block; padding-bottom: 10px; font-weight: bold; }
.line_name { display: inline-block; width: 75px; text-align: right; padding-right: 10px; color: #555; }

.student_blog_wrap { outline: 1px solid #eee; width: 90%; margin: 0 auto; min-height: 175px; margin-top: 25px; }
.student_blog_data { margin-top: 25px; }

.student_post_item_wrap { padding: 25px; }
.student_post_item_data { border-bottom: 1px solid #999; }
a:hover .student_post_item_data { border-bottom: 1px solid #222; }

</style>

<header class="student_header_wrap">

</header><!-- . student_header_wrap - -->

<div class="main_body_wrap">
  <div class="page_title">Student</div>

  <div class="student_contact_info_wrap">
    <div class="student_contact_info_data">
      <span class="head_name">Info</span>
      <div class="student_email_wrap">
        <span class="line_name">Name</span> 
        [!student_profile_data.profile_name!]
      </div>
      <div class="student_email_wrap">
        <span class="line_name">Email</span> 
        [!student_profile_data.profile_email!]
      </div>
      <div class="student_phone_wrap">
        <span class="line_name">Phone</span>
        [!student_profile_data.profile_phone!]
      </div>
      <div class="student_link_wrap">
        <span class="line_name">Link</span>
        [!student_profile_data.profile_link!]
      </div>
      <div class="student_link_wrap">
        <span class="line_name">Bio</span>
        [!student_profile_data.profile_bio!]
      </div>
    </div><!-- . student_contact_info_data - -->
  </div><!-- . student_contact_info_wrap - -->

<div class="page_title">Blog Posts</div>

  <div class="student_blog_wrap">
    <div class="student_blog_data">
      <div class="student_post_item_wrap" ng-repeat="item in student_blog_data">
        <a href="../../blog_post_id?[!item.data_id!]">
          <div class="student_post_item_data">
            <p>[!item.blog_post_name!]</p>
          </div><!-- . student_post_item_data - -->
        </a>
      </div><!-- . student_post_item_wrap - -->
    </div><!--- . student_blog_data - -->
  </div><!-- . student_blog_wrap - -->

</div><!-- . main_body_wrap - -->
'''


student_page_create_html = '''<style>

.student_header_wrap { padding: 25px; width: 90%; margin: 0 auto; outline: 1px solid #eee; margin-bottom: 45px;}
.student_header_photo { display: inline-block; margin: 25px; width: 250px; }
.student_header_photo img { width: 100%; }
.main_logo_wrap { display: inline-block; width: 225px; margin: 25px; }
.main_logo_wrap img { width: 100%; }

.main_body_wrap { min-height: 550px; }
.user_image_wrap { text-align: center; margin-bottom: 25px; }
.page_title { color: #00796B; text-align: center; }


.student_contact_info_wrap { border: 25px solid #FAFAFA; margin-top: 45px; }
.student_contact_info_data { border: 1px solid #ccc; padding: 10px; }
.head_name { display: inline-block; padding-bottom: 10px; font-weight: bold; }
.line_name { display: inline-block; width: 75px; text-align: right; padding-right: 10px; }
input[type="text"] {  }

</style>

<header class="student_header_wrap">

</header><!-- . student_header_wrap - -->

<div class="main_body_wrap">
  <div class="user_image_wrap">
    <img src="../../pics/jumpgirl.jpg" />
  </div>
  <div class="page_title">Create New Student User Profile</div>

  <div class="student_contact_info_wrap">
    <div class="student_contact_info_data">
      <form action="../../new_student_user" method="post">
      <span class="head_name">Info</span>
      <div class="student_email_wrap">
        <span class="line_name">Name</span> 
        <input type="text" name="profile_name" />
      </div>
      <div class="student_email_wrap">
        <span class="line_name">Email</span> 
        <input type="text" name="profile_email" />
      </div>
      <div class="student_phone_wrap">
        <span class="line_name">Phone</span>
        <input type="text" name="profile_phone" />
      </div>
      <div class="student_link_wrap">
        <span class="line_name">Link</span>
        <input type="text" name="profile_link" />
      </div>
      <div class="student_link_wrap">
        <span class="line_name">Short Bio</span>
        <textarea name="profile_bio"></textarea>
      </div>
      <div class="submit_button_wrap">
        <input type="submit">
      </div>
    </form>
    </div><!-- . student_contact_info_data - -->
  </div><!-- . student_contact_info_wrap - -->

</div><!-- . main_body_wrap - -->
'''




doctor_profile_page_html = '''<style>

.profile_header_wrap { padding: 25px; width: 90%; margin: 0 auto; outline: 1px solid #eee; margin-bottom: 45px; }
.profile_header_photo { display: inline-block; margin: 25px; width: 250px; }
.profile_header_photo img { width: 100%; }
.main_logo_wrap { display: inline-block; width: 225px; margin: 25px; }
.main_logo_wrap img { width: 100%; }

.main_body_wrap { min-height: 550px; }
.page_title { color: #00796B; }


.profile_contact_info_wrap { border: 25px solid #FAFAFA; margin-top: 45px; margin-bottom: 50px; }
.profile_contact_info_data { border: 1px solid #ccc; padding: 10px; }
.head_name { display: inline-block; padding-bottom: 10px; font-weight: bold; }
.line_name { display: inline-block; width: 75px; text-align: right; padding-right: 10px; color: #555; }

.profile_blog_wrap { outline: 1px solid #eee; width: 600px; min-height: 175px; margin-top: 25px; }
.profile_blog_data { margin-top: 25px; }

.profile_post_item_wrap { padding: 25px; }
.profile_post_item_data { border-bottom: 1px solid #999; }
a:hover .profile_post_item_data { border-bottom: 1px solid #222; }

</style>

<header class="profile_header_wrap">

</header><!-- . student_header_wrap - -->

<div class="main_body_wrap">
  <div class="page_title">Doctor</div>

  <div class="profile_contact_info_wrap">
    <div class="profile_contact_info_data">
      <span class="head_name">Info</span>
      <div class="profile_email_wrap">
        <span class="line_name">Name</span> 
        [!doctor_profile_data.data_id!]
      </div>
      <div class="profile__email_wrap">
        <span class="line_name">Email</span> 
        [!doctor_profile_data.profile_email!]
      </div>
      <div class="profile_phone_wrap">
        <span class="line_name">Phone</span>
        [!doctor_profile_data.profile_phone!]
      </div>
      <div class="profile_link_wrap">
        <span class="line_name">Link</span>
        [!doctor_profile_data.profile_link!]
      </div>
    </div><!-- . profile_contact_info_data - -->
  </div><!-- . profile_contact_info_wrap - -->

<div class="page_title">Blog Posts</div>

  <div class="profile_blog_wrap">
    <div class="profile_blog_data">
      <div class="profile_post_item_wrap" ng-repeat="item in profile_blog_data">
        <a href="../../blog_post_id?[!item.data_id!]">
          <div class="profile_post_item_data">
            <p>[!item.blog_post_name!]</p>
          </div><!-- . profile_post_item_data - -->
        </a>
      </div><!-- . profile_post_item_wrap - -->
    </div><!--- . profile_blog_data - -->
  </div><!-- . profile_blog_wrap - -->

</div><!-- . main_body_wrap - -->
'''


doctor_page_create_html = '''<style>

.doctor_header_wrap { padding: 25px; width: 90%; margin: 0 auto; outline: 1px solid #eee; margin-bottom: 45px; }
.doctor_header_photo { display: inline-block; margin: 25px; width: 250px; }
.doctor_header_photo img { width: 100%; }
.main_logo_wrap { display: inline-block; width: 225px; margin: 25px; }
.main_logo_wrap img { width: 100%; }

.main_body_wrap { min-height: 550px; }
.user_image_wrap { text-align: center; margin-bottom: 25px; }
.page_title { color: #00796B; text-align: center; }


.doctor_contact_info_wrap { border: 25px solid #FAFAFA; margin-top: 45px; }
.doctor_contact_info_data { border: 1px solid #ccc; padding: 10px; }
.head_name { display: inline-block; padding-bottom: 10px; font-weight: bold; }
.line_name { display: inline-block; width: 75px; text-align: right; padding-right: 10px; }
input[type="text"] { }

</style>

<header class="doctor_header_wrap">

</header><!-- . doctor_header_wrap - -->

<div class="main_body_wrap">
    <div class="user_image_wrap">
    <img src="../../pics/jumpgirl.jpg" />
  </div>
  <div class="page_title">Create New Doctor User Profile</div>

  <div class="doctor_contact_info_wrap">
    <div class="doctor_contact_info_data">
      <form action="../../new_doctor_user" method="post">
      <span class="head_name">Info</span>
      <div class="doctor_email_wrap">
        <span class="line_name">Name</span> 
        <input type="text" name="student_name" />
      </div>
      <div class="doctor_email_wrap">
        <span class="line_name">Email</span> 
        <input type="text" name="student_email" />
      </div>
      <div class="doctor_phone_wrap">
        <span class="line_name">Phone</span>
        <input type="text" name="student_phone" />
      </div>
      <div class="doctor_link_wrap">
        <span class="line_name">Link</span>
        <input type="text" name="student_link" />
      </div>
      <div class="doctor_link_wrap">
        <span class="line_name">Short Bio</span>
        <textarea name="student_bio"></textarea>
      </div>
      <div class="submit_button_wrap">
        <input type="submit">
      </div>
    </form>
    </div><!-- . doctor_contact_info_data - -->
  </div><!-- . doctor_contact_info_wrap - -->

</div><!-- . main_body_wrap - -->
'''

















new_student_user_page_html = '''
<style>


</style>

<div class="main_body_wrap">
  <div class="page_title">New Student Profile</div>

<div class="sign_in_wrap" ng-show="user_name=='No User'">
  <p>Welcome,<br />please sign in with a Google Account &nbsp;
  <i class="fa fa-user" aria-hidden="true"></i></p>
</div>

<div class="new_student_form_wrap">
  <form action="../../new_student_user" method="post">
    <table>
      <tr>
        <td class="label">Full Name</td>
        <td class="input"><input type="text" name="student_name"></td>
      </tr>
      <tr>
        <td></td>
        <td style="text-align:right"><input type="submit"></td>
      </tr>
    <table>
  </form>
</div><!-- . new_student_form_wrap - -->


</div><!-- . main_body_wrap - -->

'''








#----------------------------------------------#
#           Landing HTML Page Code             #
#----------------------------------------------#


front_page_html = '''
<img src="../../pics/logo.jpg" />

'''












main_page_html = '''
<style>
.main_body_wrap { padding-bottom: 15px; }
.option_wrap { margin-top: 25px; text-align: center; }
.enter_option { border: 1px solid #aaa; width: 80px; text-align: center; border-radius: 3px; margin: 10px; padding: 5px; display: inline-block; cursor: pointer; font-size: 14px; color: #777; }
.enter_option:hover { color: #111; border: 1px solid #bbb; }
.user_signin_wrap { text-align: center; margin-top: 45px; cursor: pointer; }

.main_image_wrap { display: inline-block; vertical-align: top; margin-top: 25px; margin-left: 100px; text-align: center; height: 270px; }
.main_image_wrap img { width: 100px; margin-top: 50px; }

.image_wrap { width: 550px; height: 200px; font-size: 14px; letter-spacing: 0.04em; margin:0 auto; text-align: center; padding: 10px; padding-bottom: 25px; }
.image_wrap img { width: 175px; margin-top: 90px; }
.vision_wrap p { text-align: justify; }

.vision_wrap_pic { width: 50px; }
.vision_tag_line { font-size: 15px; text-align: center; padding-top: 15px; color: #00796B; }

.header {text-align:center;}
.header img { width: 85%; margin-top: 25px;}

.main_logo_wrap { width: 300px; margin: 0 auto; }
.main_logo_wrap img { width: 100%; }

.next_row_wrap { margin-left: 85px; display: inline-block; margin-top: 50px; width: 300px; }

.mission_text_wrap { text-align: center;   font-size: 14px; letter-spacing: 0.04em;  
   font-size: 14px; margin-top: 75px; }
.kight_wrap {}
.mission_text_wrap img {width: 150px; margin-top:150px; margin-right: 700px;}
.mission_text_wrap ul { padding: 25px; padding-top: 0; color: #66BB6A; text-align: left; }
.mission_text_wrap ul li span { color: #102138; }
.mission_text_wrap p { text-align: justify; }

.core_values_wrap { text-align: center; padding: 25px;font-size: 14px; 
  letter-spacing: 0.04em; 
   margin-bottom: 10px; padding-bottom: 20px; margin-left: -25px;}

.man_wrap img { width: 125px; margin-top: 150px; margin-left: 25px;}

.core_values_wrap ul { padding: 25px; padding-top: 0; color: #66BB6A; text-align: left; }
.core_values_wrap ul li span { color: #102138; }
.core_values_wrap p { text-align: justify; }

   /*.core_values_wrap ol li span { color: #102138; font-size: 14px; }
.core_values_wrap ol { color: #102138; font-size: 20px; }*/

.newsletter_join_wrap { border-top: 2px solid #102138; padding-left: 55px; padding-bottom: 20px; margin-bottom: 10px; padding-left:; margin-top: 100px; text-align: center;}
.newsletter_join_wrap input { height: 30px; width: 250px; padding-left: 20px;}
button.join_button { display: inline-block; border: 5px solid #999; border-radius: 5px; width: 95px; text-align: center; cursor: pointer; background-color: white; height: 27px; margin-top: 25px; }
button.join_button:hover { border: 1px solid #7fff00; background-color:#4caf50; }


/*.part_title { font-size: 24px; font-family: 'Source Code Pro'; color: #00796B; }

.tag_line { font-size: 18px; text-align: center; color: #00796B; }*/
.join_text { text-align:left; margin-left: 30%; }
.bottom_image_wrap img { height: 105px; margin: 15px; }

.youtube_link_wrap { text-align: center; padding-top: 25px; }
.fa-youtube { font-size: 44px; }
.fa-youtube:hover { color: red; cursor: pointer; }


.social_wrap { margin-top: 20px; }
.social_item_wrap { display: inline-block; margin-left: 50px; margin-right: 50px; margin-top: 25px; margin-bottom: 25px; }
.social_item_wrap:hover a { text-decoration: none; }


.video_item_wrap { border: 1px solid #eee; width: 200px; height: 225px; display: inline-block; margin: 10px; padding: 5px;  }

.video_item_data { font-size: 12px; text-align: center; }
.doctor_name { font-weight: bold; text-align: left; font-size: 14px; }

.video_item_wrap img { width: 100%; }
.video_item_wrap a { color: #102138; }
.video_item_wrap:hover a { text-decoration: none; color: #102138; }
.video_item_wrap:hover { border: 1px solid #102138; }

.video_still_wrap { overflow: hidden; width: 100%; }
.video_still_wrap img { width: 110%; height: 110%; filter: sepia(40%); }

</style>

  <header>
    <div class="main_logo_wrap"><img src="../../pics/logo.jpg" /></div>
    <div class="header"><img src="../../pics/earth4.jpg" />
  </header>

  

<div class="image_wrap"><img src="../../pics/the_all_seeing_eye_by_lylly55.jpg" />
 </div>

<div class="vision_wrap">
 <p><span class="part_title">Vision</span><br />Cultivating and developing an abundant mindset within students who will become a community of chiropractic doctors with the freedom to open their practice of their dreams and impact the world according to their core values. Stripped of the stresses caused by student debt and able to embrace limitless possibilities.</p>
</div>
<div class="image_wrap">
<div class="main_image_wrap"><img src="../../pics/tree2.JPEG" /></div>

  <div class="vision_tag_line">Join The Chiropractic Revolution And Set the Stage for Financial Freedom!</div>
</div>


<!-- <div class="next_row_wrap">
 -->

<div class="mission_text_wrap">
<div class="knight_wrap"><img src="../../pics/knight2.jpg" /></div>

 
  
  <p><span class="part_title">Mission</span>
  <ul>
    <li><span>Support students and chiropractors build their personal brand</span></li>
    <li><span>Create a chiropractic culture that promotes personal greatness</span></li>
    <li><span>Provide mentorship opportunities for students</span></li>
    <li><span>Help students graduate debt free</span></li>
    <li><span>Provide affordable housing for chiropractic students and recent graduates</span></li>
    <li><span>Create an endowment that provides micro financing for chiropractic students</span></li>
    <li><span>Connecting DC2Be’s through a dynamic platform where student produced blogs, videos and podcasts are shared</span></li>
  </ul></p>
</div>

 <div class="man_wrap"><img src="../../pics/f3cb858652d83e76104e705ebcaa0359.jpg" /></div>
 
 
<div class="core_values_wrap">

 <p><span class="part_title">Core Values</span><br /><ul>
   <li><span>Community is created through diversity of opinions and backgrounds</span></li>
   <li><span>Your voice matters, be part of the conversation</span></li>
   <li><span>The future of the chiropractic profession begins in school</span></li>
   <li><span>Learn to over deliver value, embrace and drive innovation while in school</span></li>
   <li><span>Promote creativity, curiosity and fun within the chiropractic community</span></li>
   <li><span>Provide resources for creating content and helping students build their personal brand</span></li>
   <li><span>Create and sustain open and honest relationships</span></li>
   <li><span>Promote personal development and accountability in words, thoughts and behavior</span></li>
   <li><span>Ignite students innate passion and persistence</span></li>
   <li><span>Do more with less through creating a web of collaboration</span></li>
 </ul>
 </p>
</div>


<div class="newsletter_join_wrap">
<div class="join_text">
    Join The Newsletter</div>
    <form action="https://dc2berevolution.us13.list-manage.com/subscribe/post?u=3df7cec3ff1129da82bb9faa8&amp;id=b7f2b3ee20" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate method="post">
      <input placeholder="your email address" name="EMAIL" class="required email" id="mce-EMAIL" type="email" />
      <button type="submit" class="join_button">Join</button>
    </form>
  </div>


  <div class="social_item_wrap">
      <a href="https://www.facebook.com/DC2BeRev" target="_blank">
        <img src="../../pics/logo_facebook_1.png" /> &nbsp;
        <img src="../../pics/logo_facebook_2.png" />
        <img src="../../pics/logo_youtube.png"  />
        <p>Like the Facebook Page</p>
      </a>
    </div>





'''
upload_video_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <header class="hi"><span class="color_b">Video for [!exercise_name!]</span></header>
    <article class="form_wrap">
      <form action="{0}" enctype="multipart/form-data" method="post">
        <table>
          <tr class="hide">
            <td class="label">data_id</td>
            <td class="input"><input type="text" name="data_id" ng-model='data_id' required /></td>
          </tr>
          <tr>
            <td class="label">Upload Video</td>
            <td class="input"><input type="file" name="video_file"/></td>
          </tr>
          <tr>
            <td></td>
            <td style="text-align:right">
              <a href="/manage/exercise"><button type="button">Cancel</button></a>
              <input type="submit" value="Add Exercise Video" />
            </td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap -
  </div><!-- - .main_wrap - -->  
'''




 


manage_blog_page_html = '''
<style>

.publish_blog_form_wrap { width: 600px; margin: 0 auto; padding-bottom: 75px; }
.publish_blog_form_data { border: 25px solid #eee; padding: 50px; padding-top: 75px; min-height: 250px; }

form { outline: 1px solid #eee; width: 400px; margin: 0 auto; padding: 25px; }
td.label { text-align: right; padding-right: 10px; font-size: 14px; }
td.input { width: 250px; }
input[type="text"] { width: 275px; height: 20px; }
textarea { width: 275px; height: 175px; }

</style>

<div class="publish_blog_form_wrap">
  <div class="publish_blog_form_data">
    <p class="page_title">Manage Blog Posts</p>

    <div class="post_list_wrap">
      <div class="post_list_data">
        <div class="post_item_wrap" ng-repeat="item in student_blog_data">
          <a href="../../blog_post_id?[!item.data_id!]"><div class="post_item_data">
            <p>[!item.blog_post_name!]</p>
          </div><!-- . post_item_data - --></a>
        </div><!-- . post_item_wrap - -->
      </div><!-- . post_list_data - -->
    </div><!-- . post_list_wrap - -->

  </div><!-- . publish_blog_form_data - -->
</div><!-- . publish_blog_form_wrap - -->
'''






publish_page_html = '''<style>
.main_body_wrap { padding-bottom: 15px; }
.option_wrap { margin-top: 25px; text-align: center; }
.enter_option { border: 1px solid #aaa; width: 80px; text-align: center; border-radius: 3px; margin: 10px; padding: 5px; display: inline-block; cursor: pointer; font-size: 14px; color: #777; }
.enter_option:hover { color: #111; border: 1px solid #bbb; }
.user_signin_wrap { text-align: center; margin-top: 45px; cursor: pointer; }

.main_image_wrap { display: inline-block; vertical-align: top; margin-left: 50px; text-align: center; height: 400px; }
.main_image_wrap img { width: 200px; margin-top: 55px; }
.vision_wrap { width: 350px; height: 400px; display: inline-block; font-size: 14px; letter-spacing: 0.04em; margin-left: 45px; border-bottom: 3px solid #102138; text-align: center; padding: 5px; padding-bottom: 25px; }

.vision_wrap img { width: 300px; }
.vision_wrap p { text-align: justify; }

header { }
header img { width: 100%; }

.next_row_wrap { margin-left: 75px; display: inline-block; margin-top: 50px; width: 300px; }
.mission_text_wrap { text-align: center; width: 375px; display: inline-block; font-size: 14px; letter-spacing: 0.04em; vertical-align: top; margin-left: 70px; font-size: 14px; margin-top: 50px; }
.mission_text_wrap ul { padding: 15px; padding-top: 0; color: #66BB6A; text-align: left; }
.mission_text_wrap ul li span { color: #102138; }
.mission_text_wrap p { text-align: justify; }

.newsletter_join_wrap { padding-left: 25px; padding-bottom: 37px; margin-bottom: 45px; border-bottom: 3px solid #102138; text-align: left; padding-right: 25px; }
.newsletter_join_wrap input { height: 20px; width: 200px; padding-left: 10px; }
.join_button { display: inline-block; border: 1px solid #999; border-radius: 5px; width: 75px; text-align: center; cursor: pointer; margin-top: 20px;}
.join_button:hover { border: 1px solid #333; }

.core_values_wrap { width: 625px; padding: 10px; margin: 0 auto; font-size: 14px; line-height: 28px; }

.core_values_wrap ol { color: #102138; font-size: 20px; }
.core_values_wrap ol li span { color: #102138; font-size: 14px; }

.part_title { font-size: 24px; font-family: 'Source Code Pro'; color: #00796B; }

.tag_line { font-size: 18px; text-align: center; color: #00796B; }

.bottom_image_wrap img { height: 105px; margin: 15px; }

.youtube_link_wrap { text-align: center; padding-top: 25px; }
.fa-youtube { font-size: 44px; }
.fa-youtube:hover { color: red; cursor: pointer; }

.video_item_wrap { border: 1px solid #eee; width: 100px; height: 100px; }

</style>

  <header>
    <img src="../../pics/earth4.jpg" />
  </header>


<div class="vision_wrap">
  <img src="../../pics/logo.jpg" />
 <p><span class="part_title">Vision</span><br />Cultivating and developing an abundance mindset within students with who will become a community of chiropractic doctors with the freedom to open the practice of their dreams and impact the world according to their core values. Stripped of the stresses caused by student debt and able to embrace limitless possibilities.</p>
</div><!-- . vision_wrap - -->

<div class="main_image_wrap"><img src="../../pics/IMG_4874.JPG" />
  <div class="newsletter_join_wrap">
    <p>Join The Newsletter</p>
    <input placeholder="your email address" /> <div class="join_button">Join</div>
  </div><!-- . newsletter_join_wrap - -->
  </div>

<div class="next_row_wrap">
  <img src="../../pics/IMG_4876.JPG" width="300px;" />
  <p class="tag_line">Empowering The Next Generation<br />of Chiropractic Doctors</p>
  <p><img src="../../pics/image_one.jpg" width="300px;" /></p>
</div>
<div class="mission_text_wrap">

  <img src="../../pics/bw_img1.jpg" />

  <p><span class="part_title">Mission</span>
  <ul>
    <li><span>Support students and chiropractors build their personal brand</span></li>
    <li><span>Create a chiropractic culture that promotes personal greatness</span></li>
    <li><span>Provide mentorship opportunities for students</span></li>
    <li><span>Help students graduate debt free</span></li>
    <li><span>Provide affordable housing for chiropractic students and recent graduates</span></li>
    <li><span>Create an endowment that provides micro financing for chiropractic students</span></li>
    <li><span>Connecting DC2Be’s through a dynamic platform where student produced blogs, videos and podcasts are shared</span></li>
  </ul></p>
</div><!-- . mission_text_wrap - -->


<div class="youtube_link_wrap">
  <a href="https://www.youtube.com/channel/UCtlEfo4PHGw1hkept5WAw1g"><i class="fa fa-youtube"></i></a>
  <p>View our YouTube Chanel</p>

  <div class="video_list_wrap">
    <div class="video_item_wrap" ng-repeat="item in video_list">[! item.hi !]</div>
  </div><!-- . video_list_wrap - -->

</div><!-- . youtube_link_wrap - -->

<div class="main_body_wrap">

<div class="core_values_wrap">

 <p><span class="part_title">Core Values</span><br /><ol>
   <li><span>Community is created through diversity of opinions and backgrounds</span></li>
   <li><span>Your voice matters, be part of the conversation</span></li>
   <li><span>The future of the chiropractic profession begins in school</span></li>
   <li><span>Learn to over deliver value, embrace and drive innovation while in school</span></li>
   <li><span>Promote creativity, curiosity and fun within the chiropractic community</span></li>
   <li><span>Provide resources for creating content and helping students build their personal brand</span></li>
   <li><span>Create and sustain open and honest relationships</span></li>
   <li><span>Promote personal development and accountability in words, thoughts and behavior</span></li>
   <li><span>Ignite students innate passion and persistence</span></li>
   <li><span>Do more with less through creating a web of collaboration</span></li>
 </ol>
 </p>

 </div><!-- . core_values_wrap - -->

</div><!-- . main_body_wrap - -->
'''



#----------------------------------------------#
#          About  HTML Pages                   #
#----------------------------------------------#

about_page_html = '''<style>
.main_wrap { text-align: center; }
.body_text_wrap { font-size: 14px; letter-spacing: 0.04em; margin-top: 35px; text-align: justify; padding-bottom: 75px; }
</style>
<div class="top_logo_wrap"><img src="../../pics/IMG_4885.JPG" /></div>
<div class="main_body_wrap">

<div class="body_text_wrap">
 <p><span style="font-size:18px;font-family: 'Source Code Pro';">Vision</span><br />
Cultivating and developing an abundance mindset within students with who will become a community of chiropractic doctors with the freedom to open the practice of their dreams and impact the world according to their core values. Stripped of the stresses caused by student debt and able to embrace limitless possibilities.</p>

 <p><span style="font-size:18px;font-family: 'Source Code Pro';">Mission</span><br />
Support students and chiropractors build their personal brand
Create a chiropractic culture that promotes personal greatness
Provide mentorship opportunities for students
Help students graduate debt free
Provide affordable housing for chiropractic students and recent graduates
Create an endowment that provides micro financing for chiropractic students
Connecting DC2Be’s through a dynamic platform where student produced blogs, videos and podcasts are shared</p>

 <p><span style="font-size:18px;font-family: 'Source Code Pro';">Core Values</span><br /><ol>
   <li>Community is created through diversity of opinions and backgrounds</li>
   <li>Your voice matters, be part of the conversation</li>
   <li>The future of the chiropractic profession begins in school</li>
   <li>Learn to over deliver value, embrace and drive innovation while in school</li>
   <li>Promote creativity, curiosity and fun within the chiropractic community</li>
   <li>Provide resources for creating content and helping students build their personal brand</li>
   <li>Create and sustain open and honest relationships</li>
   <li>Promote personal development and accountability in words, thoughts and behavior</li>
   <li>Ignite students innate passion and persistence</li>
   <li>Do more with less through creating a web of collaboration</li>
 </ol>
 </p>

 <p><span style="font-size:18px;font-family: 'Source Code Pro';">Biographies</span><br />

Noah Volz loves to learn and create. Writing articles for Life Lines Student Newspaper he has started interviewing chiropractors and writing articles to help students to survive chiropractic school. As a student at Life West Chiropractic College he is involved by being a president of the LCCW yoga club and treasurer of the LCCW NUCCA club.</p>
  </div><!-- . body_text_wrap - -->
</div><!-- . main_body_wrap - -->
'''

faq_page_html = '''<style>
.main_wrap { text-align: center; }
</style>
<div class="top_logo_wrap"><img src="../../pics/logo.jpg" /></div>
<div class="main_body_wrap">
  FAQ Page
</div><!-- . main_body_wrap - -->
'''

contact_page_html = '''<style>
.main_wrap { text-align: center; }
</style>
<div class="top_logo_wrap"><img src="../../pics/logo.jpg" /></div>
<div class="main_body_wrap">
  Contact Page
</div><!-- . main_body_wrap - -->
'''

legal_page_html = '''<style>
.main_wrap { text-align: center; }
</style>
<div class="top_logo_wrap"><img src="../../pics/logo.jpg" /></div>
<div class="main_body_wrap">
  Legal Page
</div><!-- . main_body_wrap - -->
'''




#----------------------------------------------#
#            Doctor HTML Page Code             #
#----------------------------------------------#

doctor_nav_html = '''
<a href="../../new/profile_doctor"><div>Create New Profile</div></a>
<a href="."><div>View Doctor Profile</div></a><br />
<a href="."><div>Paitent Dashboard</div></a>
<a href="."><div>Discount Offers</div></a>
<a href="."><div>Membership/s</div></a>
<a href="."><div>Donations</div></a>
'''

doctor_page_html = '''<style>


</style>

<p align="center"><img src="../../pics/IMG_4879.JPG" width="300px;" /></p>


<div class="main_body_wrap">
  <div class="page_title">Doctor</div>



</div><!-- . main_body_wrap - -->
'''



new_doctor_user_page_html = '''
<style>


</style>

<div class="main_body_wrap">
  <div class="page_title">New Doctor Profile</div>

<div class="sign_in_wrap" ng-show="user_name=='No User'">
  <p>Welcome,<br />please sign in with a Google Account &nbsp;
  <i class="fa fa-user" aria-hidden="true"></i></p>
</div>

<div class="new_user_form_wrap">
  <form action="../../new_doctor_user" method="post">
    <table>
      <tr>
        <td class="label">Full Name</td>
        <td class="input"><input type="text" name="doctor_name"></td>
      </tr>
      <tr>
        <td></td>
        <td style="text-align:right"><input type="submit"></td>
      </tr>
    <table>
  </form>
</div><!-- . new_student_form_wrap - -->


</div><!-- . main_body_wrap - -->

'''


#----------------------------------------------#
#            Store HTML Page Code              #
#----------------------------------------------#

store_page_html = '''<style>


</style>

<div class="main_body_wrap">
  <div class="page_title">Store</div>


</div><!-- . main_body_wrap - -->
'''


#----------------------------------------------#
#           Contact  page                      #
#----------------------------------------------#

contact_success_page_html = '''
  <div class="main_wrap-[!layout_style!]">
  <h2>Your question has been submitted.</h2>
  <h2>We'll reply as soon as possible.</h2>
  </div><!-- .main_wrap -->
'''


#----------------------------------------------#
#             Other Pages                      #
#----------------------------------------------#

login_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <p>Sign in with your Google account</p>
  </div><!-- .main_wrap -->
'''

manage_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <p>Choose a data set from the menu to edit</p>
  </div><!-- .main_wrap -->
'''



#----------------------------------------------#
#    Programs Signup and Payment               #
#----------------------------------------------#

silver_brozen_coupon_limit = 10


confirm_signup_page_html = '''
  <div class="main_wrap-[!layout_style!]">
    <p>You have chosen the [!program_chosen!] Program ($[!price!]/month).</p>
    <button ng-click="back2programs();">Cancel</button>
    <button ng-click="go2payment();">Go to Payment</button>
  </div><!-- .main_wrap -->
'''

payment_page_html = '''
  <style>
  .form_wrap { text-align: center; width: 300px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td.input { font-size: 14px; text-align: left; padding-left: 10px; }
  input[name="client_name"], input[name="client_phone"] { width: 150px; height: 16px; }
  textarea { width: 150px; height: 50px; }
  .form_title { background: #0D47A1; padding: 10px 0; color: #fff; text-align: center; width: 100%; }
  .payment-errors { color: red; }
  .stripe_img { margin: 25px auto; text-align: center; }
  button[type='submit'] { border-radius:0; padding: 5px; font-size: 12px; }
  </style>
  <div class="main_wrap-[!layout_style!]">
  <article class="form_wrap">
    <div class="form_title">
      <h3>[!program_chosen!] Program</h3>
      <h3>Price: $[!price!]/month</h3>
    </div>
    <form action="/charge_card/" id="payment-form" method="post">
      <span class="payment-errors"></span>
      <span class="payment-errors" ng-show="program_status=='Active'&&stripe_cus_id&&stripe_subscription_id">You have already enrolled in a program.</span>
    <table>
      <tr>
        <td class="label">Name*</td>
        <td class="input"><input type="text" name="client_name" required/></td>
      </tr>
      <tr class="hide">
        <td class="label">Email*</td>
        <td class="input"><input type="text" name="client_email" ng-model="client_email" required/></td>
      </tr>
      <tr class="hide">
        <td class="label">Program*</td>
        <td class="input"><input type="text" name="client_program" ng-model="program_chosen" required/></td>
      </tr>
      <tr class="hide">
        <td class="label">Price*</td>
        <td class="input"><input type="text" name="amout" ng-model="price" required/></td>
      </tr>     
      <tr>
        <td class="label">Phone</td>
        <td class="input"><input type="text" name="client_phone" /></td>
      </tr>   
      <tr>
        <td class="label">Address</td>
        <td class="input"><textarea type="text" name="client_address"></textarea></td>
      </tr>   
      <tr>
        <td class="label">Card Number*</td>
        <td class="input"><input type="text" size="20" data-stripe="number"/></td>
      </tr>
      <tr>
        <td class="label">CVC*</td>
        <td class="input"><input type="text" size="4" data-stripe="cvc"/></td>
      </tr>
      <tr>
        <td class="label">Expiration (MM/YYYY)*</td>
        <td class="input">
          <input type="text" size="2" data-stripe="exp-month"/>
          <span> / </span>
          <input type="text" size="4" data-stripe="exp-year"/>
        </td>
      </tr>
      <tr>
        <td></td>
        <td style="text-align:right"><button type="submit" ng-disabled="program_status=='Active'&&stripe_cus_id&&stripe_subscription_id">Subscribe to Program</button></td>
      </tr>
     </table>
    </form>
    <div class="stripe_img"><img style="width:200px;" src='/pics/stripe.png'></div>
  </article><!-- - /form_wrap - -->
  </div><!-- .main_wrap -->
'''


payment_success_page_html = '''
  <div class="main_wrap-[!layout_style!]">
  <h2>Thank you for your payment.</h2>
  <h2>You will recieve an email reciept.</h2>
  </div><!-- .main_wrap -->
'''

cancel_program_success_page_html = '''
  <div class="main_wrap-[!layout_style!]">
  <h2>Your have quit the program.</h2>
  </div><!-- .main_wrap -->
'''

change_credit_card_page_html = '''
  <style>
  .form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px;text-align: center; }
  form { padding: 15px 45px; }
  tr { height: 32px; }
  td.label { font-size: 14px; text-align: right; padding-right: 10px; }
  td.input { font-size: 14px; text-align: left; padding-left: 10px; }
  .form_title { background: #0D47A1; padding: 10px; color: #fff; }
  .payment-errors { color: red; }
  .stripe_img { margin: 25px auto; }
  button[type='submit'] { border-radius: 0; padding: 5px; font-size: 12px; }
  </style>
  <div class="main_wrap-[!layout_style!]">
  <article class="form_wrap">
    <div class="form_title">
      <h3>Current Card</h3>
      <h3>****[!current_card_last4!]</h3>
    </div>
    <form action="/change_card/" id="payment-form" method="post">
      <span class="payment-errors"></span>
      <span class="payment-errors" ng-show="program_status=='Active'&&stripe_cus_id&&stripe_subscription_id">You have already enrolled in a program.</span>
    <table>  
      <tr>
        <td class="label">Card Number*</td>
        <td class="input"><input type="text" size="20" data-stripe="number"/></td>
      </tr>
      <tr>
        <td class="label">CVC*</td>
        <td class="input"><input type="text" size="4" data-stripe="cvc"/></td>
      </tr>
      <tr>
        <td class="label">Expiration (MM/YYYY)*</td>
        <td class="input">
          <input type="text" size="2" data-stripe="exp-month"/>
          <span> / </span>
          <input type="text" size="4" data-stripe="exp-year"/>
        </td>
      </tr>
      <tr>
        <td></td>
        <td style="text-align:right"><button type="submit" ng-disabled="program_status=='Active'&&stripe_cus_id&&stripe_subscription_id">Change Card</button></td>
      </tr>
     </table>
    </form>
    <img class="stripe_img" style="width:200px;" src='/pics/stripe.png'>
  </article><!-- - /form_wrap - -->
  </div><!-- .main_wrap -->
'''


change_program_success_page_html ='''
  <div class="main_wrap-[!layout_style!]">
  <h2>You have successfully changed your program. </h2>
  <h2>You will be billed the amount for the new program in the next bill.</h2>
  </div><!-- .main_wrap -->
'''

change_credit_card_success_page_html ='''
  <div class="main_wrap-[!layout_style!]">
  <h2>Your have successfully change your credit card.</h2>
  </div><!-- .main_wrap -->
'''
