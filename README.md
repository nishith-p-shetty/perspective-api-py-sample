# perspective-api-py-sample
A Python sample code to use perspective api

<div tabindex="1" class="slds-p-right_small grid-content slds-p-vertical_xx-large" data-aura-rendered-by="110:2;a">

<div data-region-name="content" data-item-id="077b7692-1ecf-4a29-9175-d26c25a9688a" data-aura-rendered-by="100:2;a">

<div data-priority="0" data-item-id="0bd048f5-045a-4856-82bd-8c67ecc2896b" class="ui-widget" data-aura-rendered-by="91:2;a">

<div data-aura-rendered-by="82:2;a" class="forceCommunityRichText forceCommunityRichTextInline" data-aura-class="forceCommunityRichText forceCommunityRichTextInline">

<div dir="ltr" data-aura-rendered-by="86:2;a" class="uiOutputRichText" data-aura-class="uiOutputRichText">

**Attributes**

<span style="color: rgb(83, 87, 101);">The Perspective API predicts the perceived impact a comment may have on a conversation by evaluating that comment across a range of emotional concepts, called attributes. When you send a request to the API, you’ll request the specific attributes you want to receive scores for. Perspective’s main attribute is TOXICITY, defined as “a rude, disrespectful, or unreasonable comment that is likely to make you leave a discussion”. </span>

<span style="color: rgb(83, 87, 101);"> </span>

<span style="color: rgb(83, 87, 101);">See all attributes, types (production or experimental), and available languages in the table below.</span>

<span style="color: rgb(83, 87, 101);"> </span>

[Join the perspective-announce email group](https://groups.google.com/forum/#!forum/perspective-announce)<span style="color: rgb(83, 87, 101);"> to stay in the loop on important information about new attributes, updates to existing attributes, deprecations, and language releases.</span>

<span style="color: rgb(83, 87, 101);"> </span>

**Production attributes**

<span style="color: rgb(83, 87, 101);">Production attributes (prod.) have been tested across multiple domains and trained on significant amounts of human-annotated comments. We recommend using production attributes for your API requests.</span>

<span style="color: rgb(83, 87, 101);"> </span>

<span style="color: rgb(83, 87, 101);"> </span>

<table width="846" style="width: 634.5pt; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;" border="0" class="ql-table-blob" data-aura-rendered-by="87:2;a">

<tbody>

<tr style="height: 42pt;">

<td style="border: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 42pt;" valign="bottom">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Attribute name</span>

</td>

<td style="border-top: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-image: initial; border-left: none; padding: 5pt 10pt; height: 42pt;" valign="bottom">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Description</span>

</td>

<td style="border-top: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-image: initial; border-left: none; padding: 5pt 10pt; height: 42pt;" valign="bottom">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Available Languages</span>

</td>

</tr>

<tr style="height: 239.25pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 239.25pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">TOXICITY</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 239.25pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">A rude, disrespectful, or unreasonable comment that is likely to make people leave a discussion.</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 239.25pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: black;">Arabic (ar), Chinese (zh), Czech (cs), Dutch (nl), </span><span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">English (en), French (fr), German (de), </span><span style="font-size: 11pt; font-family: Roboto; color: black;">Hindi (hi), Hinglish (hi-Latn), Indonesian (id), </span><span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Italian (it), </span><span style="font-size: 11pt; font-family: Roboto; color: black;">Japanese (ja), Korean (ko),</span><span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);"> </span><span style="font-size: 11pt; font-family: Roboto; color: black;">Polish (pl), </span><span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Portuguese (pt), Russian (ru), Spanish (es), Swedish (sv)</span><span style="font-family: Roboto;"></span>

</td>

</tr>

<tr style="height: 120.75pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 120.75pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">SEVERE_TOXICITY</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 120.75pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">A very hateful, aggressive, disrespectful comment or otherwise very likely to make a user leave a discussion or give up on sharing their perspective. This attribute is much less sensitive to more mild forms of toxicity, such as comments that include positive uses of curse words.</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 120.75pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(23, 43, 77); letter-spacing: -0.05pt; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">ar, zh, cs, nl, en, fr, de, hi, hi-Latn, id, it, ja, ko, pl, pt, ru, es, sv</span><span style="font-size: 11pt; font-family: Roboto;"></span>

</td>

</tr>

<tr style="height: 48.75pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 48.75pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">IDENTITY_ATTACK</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 48.75pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Negative or hateful comments targeting someone because of their identity.</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 48.75pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(23, 43, 77); letter-spacing: -0.05pt; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">ar, zh, cs, nl, en, fr, de, hi, hi-Latn, id, it, ja, ko, pl, pt, ru, es, sv</span>

</td>

</tr>

<tr style="height: 48.75pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 48.75pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">INSULT</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 48.75pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Insulting, inflammatory, or negative comment towards a person or a group of people.</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 48.75pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(23, 43, 77); letter-spacing: -0.05pt; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">ar, zh, cs, nl, en, fr, de, hi, hi-Latn, id, it, ja, ko, pl, pt, ru, es, sv</span>

</td>

</tr>

<tr style="height: 48.75pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 48.75pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">PROFANITY</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 48.75pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Swear words, curse words, or other obscene or profane language.</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 48.75pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(23, 43, 77); letter-spacing: -0.05pt; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">ar, zh, cs, nl, en, fr, de, hi, hi-Latn, id, it, ja, ko, pl, pt, ru, es, sv</span>

</td>

</tr>

<tr style="height: 48.75pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 48.75pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">THREAT</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 48.75pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Describes an intention to inflict pain, injury, or violence against an individual or group.</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 48.75pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(23, 43, 77); letter-spacing: -0.05pt; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">ar, zh, cs, nl, en, fr, de, hi, hi-Latn, id, it, ja, ko, pl, pt, ru, es, sv</span>

</td>

</tr>

</tbody>

</table>

<span style="color: rgb(83, 87, 101);">  </span>

**Experimental attributes**

<span style="color: rgb(83, 87, 101);">Experimental attributes (exp.) have not been tested as thoroughly as production attributes. We recommend using experimental attributes only in non-production environments where a human is identifying and correcting errors. We’d also appreciate your</span> [feedback](https://google-jigsaw--livepreview.na158.force.com/perspective/s/docs-contribute-feedback) <span style="color: rgb(83, 87, 101);">on these models!</span>

<span style="color: rgb(83, 87, 101);"> </span>

**Important notes on using experimental attributes:**

*   Once experimental attributes are deprecated and production attributes are created, the experimental attribute will stop working. When that happens, you will need to update the API call’s attribute name to the new production attribute name.
*   Expect language availability to change over time as we test attribute performance and move attributes to production.

<span style="color: rgb(83, 87, 101);"> </span>

<table width="846" style="width: 634.5pt; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;" border="0" class="ql-table-blob" data-aura-rendered-by="87:2;a">

<tbody>

<tr style="height: 4.5pt;">

<td style="border: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 4.5pt;" valign="bottom">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Attribute name</span>

</td>

<td style="border-top: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-image: initial; border-left: none; padding: 5pt 10pt; height: 4.5pt;" valign="bottom">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Description</span>

</td>

</tr>

<tr style="height: 46.55pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 46.55pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">TOXICITY_EXPERIMENTAL</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 46.55pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">A rude, disrespectful, or unreasonable comment that is likely to make people leave a discussion.</span>

</td>

</tr>

<tr style="height: 120.75pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 120.75pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">SEVERE_TOXICITY_EXPERIMENTAL</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 120.75pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">A very hateful, aggressive, disrespectful comment or otherwise very likely to make a user leave a discussion or give up on sharing their perspective. This attribute is much less sensitive to more mild forms of toxicity, such as comments that include positive uses of curse words.</span>

</td>

</tr>

<tr style="height: 42pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 42pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">IDENTITY_ATTACK_EXPERIMENTAL</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 42pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Negative or hateful comments targeting someone because of their identity.</span>

</td>

</tr>

<tr style="height: 42pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 42pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">INSULT_EXPERIMENTAL</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 42pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Insulting, inflammatory, or negative comment towards a person or a group of people.</span>

</td>

</tr>

<tr style="height: 42pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 42pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">PROFANITY_EXPERIMENTAL</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 42pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Swear words, curse words, or other obscene or profane language.</span>

</td>

</tr>

<tr style="height: 42pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 42pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">THREAT_EXPERIMENTAL</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 42pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Describes an intention to inflict pain, injury, or violence against an individual or group.</span>

</td>

</tr>

<tr style="height: 42pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 42pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">SEXUALLY_EXPLICIT</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 42pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Contains references to sexual acts, body parts, or other lewd content.</span>

</td>

</tr>

<tr style="height: 42pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 42pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">FLIRTATION</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 42pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Pickup lines, complimenting appearance, subtle sexual innuendos, etc.</span>

</td>

</tr>

</tbody>

</table>

<span style="color: rgb(83, 87, 101);"> </span>

**New York Times attributes**

<span style="color: rgb(83, 87, 101);">These attributes are experimental because they are trained on a single source of comments—New York Times (NYT) data tagged by their moderation team—and therefore may not work well for every use case.</span>

<span style="color: rgb(83, 87, 101);"> </span>

<table width="846" style="width: 634.5pt; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;" border="0" class="ql-table-blob" data-aura-rendered-by="87:2;a">

<tbody>

<tr style="height: 24pt;">

<td style="border: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Attribute name</span>

</td>

<td style="border-top: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-image: initial; border-left: none; padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Description</span>

</td>

<td style="border-top: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-image: initial; border-left: none; padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Language</span>

</td>

</tr>

<tr style="height: 24pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">ATTACK_ON_AUTHOR</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Attack on the author of an article or post. </span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">en</span>

</td>

</tr>

<tr style="height: 24pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">ATTACK_ON_COMMENTER</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Attack on fellow commenter.</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">en</span>

</td>

</tr>

<tr style="height: 24pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">INCOHERENT</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Difficult to understand, nonsensical.</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">en</span>

</td>

</tr>

<tr style="height: 24pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">INFLAMMATORY</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Intending to provoke or inflame.</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">en</span>

</td>

</tr>

<tr style="height: 38.25pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 38.25pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">LIKELY_TO_REJECT</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 38.25pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Overall measure of the likelihood for the comment to be rejected according to the NYT's moderation.</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 38.25pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">en</span>

</td>

</tr>

<tr style="height: 24pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">OBSCENE</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Obscene or vulgar language such as cursing.</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">en</span>

</td>

</tr>

<tr style="height: 24pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">SPAM</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Irrelevant and unsolicited commercial content.</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">en</span>

</td>

</tr>

<tr style="height: 24pt;">

<td style="border-right: 1pt solid rgb(223, 226, 229); border-bottom: 1pt solid rgb(223, 226, 229); border-left: 1pt solid rgb(223, 226, 229); border-image: initial; border-top: none; padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: &quot;Courier New&quot;; color: rgb(50, 52, 60);">UNSUBSTANTIAL</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">Trivial or short comments</span>

</td>

<td style="border-top: none; border-left: none; border-bottom: 1pt solid rgb(223, 226, 229); border-right: 1pt solid rgb(223, 226, 229); padding: 5pt 10pt; height: 24pt;" valign="top">

<span style="font-size: 11pt; font-family: Roboto; color: rgb(50, 52, 60);">en</span>

</td>

</tr>

</tbody>

</table>

<span style="color: rgb(83, 87, 101);"> </span>

**Model cards**

<span style="color: rgb(83, 87, 101);">For each production attribute, we are publishing an associated "Model card" that shares details about intended usage, attribute training processes, and evaluation results.</span>


</div>

</div>

</div>


</div>

</div>
