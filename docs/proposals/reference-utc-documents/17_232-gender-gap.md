# Proposal for Fully Gender-Inclusive Emoji

Unicode document **L2/17-232**. Authors: Charlotte Buff.

**Outcome:** A 20-page structural argument by a private individual.

Source: <https://www.unicode.org/L2/L2017/17232-gender-gap.pdf> (retrieved 2026-07-09). Text-layer word count: 5,660.

---

```text
                                       L2/17-232

                                                                                                     Proposal for Fully Gender-Inclusive Emoji

Proposal for Fully Gender-Inclusive Emoji

           Author: Charlotte Buff
Mail: irgendeinbenutzername@gmail.com

           Submitted: 2017-06-28

1. Background

Last year's Emoji 4.0 update introduced the concept of gender to the world of Unicode. Before said
version of TR 51 became a reality, I wrote to the UTC twice (L2/16-169, L2/16-193) about its
flaws, remarking that the stated goal of allowing improved gender representation would be utterly
impossible to achieve without introducing a third gender option and without enabling gender
variants for all human-form emoji rather than just for the arbitrary selection of characters that were
deemed gender-worthy by members of the Consortium at the time. Unfortunately, my comments did
not lead to any changes in the emoji documentation whatsoever, resulting in a terribly restrictive
binary gender model with random omissions that only serves to further perpetuate harmful gender
stereotypes and outdated, conservative world views.

Later, the UTC approved the encoding of three explicitly gender-neutral emoji (Hunt, L2/16-317)
that would complete the already existing male and female family member set. The optimist and
rationalist in me assumed this finally meant that the approval of all gender-neutral emoji and the
addition of the few missing gender variants would follow quickly, and that the UTC had realised
that a binary gender model based solely on clich�s is not suitable � it is the only assumption that
made sense considering the UTC's decision. But alas, U+1F9D1 ADULT, U+1F9D2 CHILD, and
U+1F9D3 OLDER ADULT remained the only third-gender emoji and the missing binary gender
options weren't considered either for Emoji 5.0.

As well as leaving feedback on various public review issues, I also wrote to the Emoji
Subcommittee several times about this glaring problem:

    � The Fourth Comment on Gendered Emoji (2017-03-11)
    � Filling the Gaps in the Emoji 5.0 Repertoire (2017-03-14)
    � Revised Proposal to Fill the Gaps in the Emoji 5.0 Repertoire (2017-03-30)
    � Response to Feedback on My Latest Proposal (2017-04-21)
    � Request for Clarification of Gendered Emoji Situation (2017-06-10)

Since I did not receive any responses to my last two submissions to this date, I am now forced to
write this proposal without knowing the ESC's current intentions so I apologize if this document
turns out to be redundant in parts.

2. Overview of Proposed Emoji

The following table illustrates quite well why the current Unicode gender repertoire does not make
any logical sense. Available gender options are marked with a , while excluded gender options are
marked with a .

Concept  Male Neutral Female
Child
                   

         1/20
                                 Proposal for Fully Gender-Inclusive Emoji

Adult                          
Older adult
Health worker                  
Student
Teacher                        
Judge
Farmer                         
Cook
Mechanic                       
Factory worker
Office worker                  
Scientist
Technologist                   
Singer
Artist                         
Pilot
Astronaut                      
Firefighter
Police officer                 
Sleuth
Guard                          
Construction worker
Royalty                        
Turban
Gua pi mao                     
Headscarf
Beard                          
Blond hair
Tuxedo                         
Veil
Pregnancy                      
Breast feeding
Christmas                      
Mage
                               

                               

                               

                               

                               

                               

                               

                               

                               

                               

                               

                               

                               

                               

                               

                               

                               

                     2/20
                                  Proposal for Fully Gender-Inclusive Emoji

Fairy                           

Vampire                         

Merperson                       

Elf                             

Genie                           

Zombie                          

Frowning                        

Pouting                         

No good gesture                 

OK gesture                      

Information desk                

Raising hand                    

Bowing                          

Face palm                       

Shrug                           

Face massage                    

Haircut                         

Walking                         

Running                         

Dancing                         

Bunny ears                      

Steamy room                     

Climbing                        

Lotus position                  

Levitating in business suit     

Golf                            

Surfing                         

Rowboat                         

Swimming                        

Ball                            

Weight lifting                  

Bicycle                         

Mountain bicycle                

Cartwheel                       

                  3/20
                        Proposal for Fully Gender-Inclusive Emoji

Wrestling             
Water polo
Handball              
Juggling
                      

                      

There is absolutely no discernible pattern here. My best guess is that the list of gender variants is
purely based on what individual people on the Consortium personally consider "normal" human
behaviour, but even that theory does not fully hold up because the same list that includes men
dressed up as playboy bunnies and women wearing a turban simultaneously excludes men in
wedding dresses and women with beards. In any case it is undeniable that the current list is
discriminatory because it pretends that people of certain genders can only dress and behave in
certain ways, and it prohibits a significant number of people from using emoji that reasonably
represent their identity, which is the exact opposite of what the UTC claimed to be working towards
with Emoji 4.0. As it currently stands gender representation in Unicode is worse than ever before.
This is not inclusion; this is tokenism.

The ESC did publish its own document concerning the matter (Davis, L2/17-071) and presented it
at UTC #151. However, the only consequence of this proposal (action item 151-A103) seemed to be
that the UTC now intents to better document the gender situation rather than make any substantial
improvements to it.

In short, I propose the addition of all emoji that are represented by a  in the above table,
amounting to 3 new characters and 32 new ZWJ sequences (Fitzpatrick variants have not been
counted). Note that the table only shows the ideal situation that should be the case according to
UTS 51. In reality however absolutely no-one has bothered yet to make their neutral emoji actually
neutral and instead just duplicated one of the other genders at random. (I say "at random" but it is
obvious that many genders were assigned according to false stereotypes.) Because of that this
proposal is not as straight-forward as most others because I am essentially asking for the addition of
emoji that have the same meaning and same visual appearance of already existing ones, while said
existing emoji need to have their established meanings changed accordingly.

For example, while U+1F931 BREAST-FEEDING is intended to be gender-neutral and has a gender-
neutral CLDR short name, all implementations that already support it render it with the same
physical features as U+1F469 WOMAN (long hair, red lips etc.), making the current default de facto
female. Vendors would therefore need to design a new neutral glyph for the default and move the
current default glyph to the proposed female version.

Because there only are three neutral emoji the majority of users likely have no idea that there are
supposed to be gender-neutral variants at all, so vendors are currently under no pressure to correct
their designs. This is made worse by the fact that the three genderless characters that do exist just
represent the most generic, featureless people possible and not actually any useful concepts,
gestures or emotions. The approval of the 19 explicitly neutral options missing (dancing, crown,
Christmas, and ZWJ professions) would force vendors to also turn their other currently binary
defaults into neutrals as to not confuse their users. It would make no sense to offer three different
variations for one half of all human-form emoji but only two for the other half. This discrepancy is
currently not as apparent to users because emoji that are missing one of the binary genders are a
small minority, and binary genders are what most people care about.

            4/20
                                                                                                                                  Proposal for Fully Gender-Inclusive Emoji

General disclaimer: This proposal is not to be interpreted as `this is how things must be done' but
rather `if I cannot prevent you from going through with this, here is the least destructive way to do
it'. My original opinion from one year ago that gender has no place in Unicode remains unchanged.
Implementing three gender options for all emoji without exceptions is the only way to minimize the
damage that has already been done, but it can never solve the underlying problem in the long run.

The three new characters are for cases where a gender pair has been encoded as atomic characters:

    � PERSON DANCING, to complement DANCER and MAN DANCING
    � PERSON WITH CROWN, to complement PRINCESS and PRINCE
    � PERSON WITH CHRISTMAS HAT, to complement FATHER CHRISTMAS and MOTHER CHRISTMAS

While PERSON WITH CROWN and PERSON WITH CHRISTMAS HAT could theoretically also be encoded as
ZWJ sequences, I do not recommend this approach. Doing so would imply that the neutral option is
some kind of unimportant, hacked-in afterthought; then we would need to decide whether the man
or the woman is the "real" default, and there is no answer to that question. Also, requiring a larger
amount of codepoints and bytes in memory to seemingly remove explicit gender connotations from
an emoji is counterintuitive and inconsistent with the rest of Unicode Emoji.

PERSON WITH CHRISTMAS HAT is an unfortunate compromise since there does not exist a non-binary
equivalent to Father Christmas to my knowledge. I would never have proposed this character if
U+1F936 MOTHER CHRISTMAS hadn't been approved for Unicode 9. MOTHER CHRISTMAS was
encoded not by popular demand but because of a perceived gender bias in emoji, which is why the
addition of a third-gender Christmas humanoid now also becomes necessary. I have decided against
calling it `Parent Christmas' because no such figure exists. While Santa Claus's wife can at least
claim to be present in a small selection of Christmas stories, I have unfortunately never come across
a holiday special starring a genderqueer Santa type.

PERSON DANCING is a strange case as well. With the addition of U+1F57A MAN DANCING it became
clear that the UTC considers U+1F483 DANCER to be female-only despite this causing compatibility
problems with Japanese carrier emoji, where KDDI offered an image that looked much closer to
today's MAN DANCING. I would much rather prefer DANCER returning to its genderless origins and
instead a new female dancer being defined, but I don't see that happening. Several vendors have
changed the genders of many of their emoji before, but DANCER is one of the most popular and
widely-used emoji in existence. Seeing how Apple effectively single-handedly defines all emoji
definitions nowadays and Apple says that U+1F483 is a woman, it is much easier to encode a new

                                                          5/20
                                                                                                                                  Proposal for Fully Gender-Inclusive Emoji

neutral dancing emoji, even if it leads to the awkward situation of having de jure two neutral
dancers, one male dancer, and no female one.

The 32 remaining emoji are to be implemented as ZWJ sequences. The 16 professions that were
first introduced in Emoji 4.0 use the usual person+object syntax, only with ADULT replacing
MAN/WOMAN to form neutral humans. The remaining concepts make use of  and  to denote
gender variants of the same character, with the unmarked base being (re)defined as neutral. Again,
emoji gender changes have occurred numerous times in the past and most of the characters that are
still missing gender options aren't exactly user favourites (or are so new that hardly anyone is aware
of their existence yet), so this should not cause too many problems.

3. Identification                              CLDR Short Name
                                               Person Dancing
3.1. CLDR Short Names                          Person with Crown
Character or Sequence                          Person with Christmas Hat
                                               Woman with Chinese Cap
PERSON DANCING                                 Man with Chinese Cap
PERSON WITH CROWN                              Woman with Veil
PERSON WITH CHRISTMAS HAT                      Man with Veil
MAN WITH GUA PI MAO + FEMALE SIGN              Woman in Tuxedo
MAN WITH GUA PI MAO + MALE SIGN                Man in Tuxedo
BRIDE WITH VEIL + FEMALE SIGN                  Woman in Suit Levitating
BRIDE WITH VEIL + MALE SIGN                    Man in Suit Levitating
MAN IN TUXEDO + FEMALE SIGN                    Pregnant Woman
MAN IN TUXEDO + MALE SIGN                      Pregnant Man
MAN IN BUSINESS SUIT LEVITATING + FEMALE SIGN  Woman Breast-Feeding
MAN IN BUSINESS SUIT LEVITATING + MALE SIGN    Man Breast-Feeding
PREGNANT WOMAN + FEMALE SIGN
PREGNANT WOMAN + MALE SIGN
BREAST-FEEDING + FEMALE SIGN
BREAST-FEEDING + MALE SIGN

                                               6/20
                                                         Proposal for Fully Gender-Inclusive Emoji

PERSON WITH HEADSCARF + FEMALE SIGN  Woman with Headscarf
PERSON WITH HEADSCARF + MALE SIGN    Man with Headscarf
BEARDED PERSON + FEMALE SIGN         Bearded Woman
BEARDED PERSON + MALE SIGN           Bearded Man
ADULT + STAFF OF AESCULAPIUS         Health Worker
ADULT + SCALES                       Judge
ADULT + AIRPLANE                     Pilot
ADULT + EAR OF RICE                  Farmer
ADULT + COOKING                      Cook
ADULT + GRADUATION CAP               Student
ADULT + MICROPHONE                   Singer
ADULT + ARTIST PALETTE               Artist
ADULT + SCHOOL                       Teacher
ADULT + FACTORY                      Factory Worker
ADULT + PERSONAL COMPUTER            Technologist
ADULT + BRIEFCASE                    Office Worker
ADULT + WRENCH                       Mechanic
ADULT + MICROSCOPE                   Scientist
ADULT + ROCKET                       Astronaut
ADULT + FIRE ENGINE                  Firefighter

The following existing emoji need to have their short names updated to reflect the necessary gender
changes.

Emoji                            Old Name                New Name
MAN WITH GUA PI MAO              Man with Chinese Cap    Person with Chinese Cap
BRIDE WITH VEIL                  Bride with Veil         Person with Veil
MAN IN TUXEDO                    Man in Tuxedo           Person in Tuxedo
MAN IN BUSINESS SUIT LEVITATING  Man in Suit Levitating  Person in Suit Levitating
PREGNANT WOMAN                   Pregnant Woman          Pregnant Person
BREAST-FEEDING                   Breast-Feeding          Person Breast-Feeding
PERSON WITH HEADSCARF            Woman with Headscarf    Person with Headscarf

3.2. CLDR Keywords

Keywords for all emoji proposed here are for the most part identical to those of the characters they
derive from, just with all references to gender adjusted accordingly.

Emoji                                Keywords
PERSON DANCING                       dance | dancing

                                     7/20
PERSON WITH CROWN                                                     Proposal for Fully Gender-Inclusive Emoji
PERSON WITH CHRISTMAS HAT
Woman with Chinese Cap        crown | fairy tail | fantasy
Man with Chinese Cap          Christmas | celebration
Woman with Veil               gua pi mao | hat | woman
Man with Veil                 gua pi mao | hat | man
Woman in Tuxedo               bride | veil | wedding
Man in Tuxedo                 groom | veil | wedding
Woman in Suit Levitating      bride | tuxedo | woman
Man in Suit Levitating        groom | man | tuxedo
Pregnant Woman                business | suit | woman
Pregnant Man                  business | man | suit
Woman Breast-Feeding          pregnant | woman
Man Breast-Feeding            pregnant | man
Woman with Headscarf          baby | breast | nursing
                              baby | breast | nursing
Man with Headscarf            headscarf | hijab | mantilla | tichel | bandana | head
                              kerchief
Bearded Woman                 headscarf | hijab | mantilla | tichel | bandana | head
Bearded Man                   kerchief
Health Worker                 beard
Judge                         beard
Pilot                         doctor | healthcare | nurse | therapist
Farmer                        justice | scales
Cook                          pilot | plane
Student                       farmer | gardener | rancher
Singer                        chef | cook
Artist                        graduate | student
Teacher                       actor | entertainer | rock | singer | star
Factory Worker                artist | palette
Technologist                  instructor | professor | teacher
Office Worker                 assembly | factory | industrial | worker
Mechanic                      coder | developer | inventor | software | technologist
Scientist                     architect | business | manager | office | white-collar
                              electrician | mechanic | plumber | tradesperson
Astronaut                     biologist | chemist | engineer | mathematician |
Firefighter                   physicist | scientist
                              astronaut | rocket
                              firefighter | firetruck

                           8/20
                                                                                                                                  Proposal for Fully Gender-Inclusive Emoji

4. Factors for Inclusion

A. Compatibility
Not applicable.

B. Expected Usage Level
Let me preface this section by stating very clearly that this factor should not and cannot apply to
this proposal in exactly the same way it does to most others. None of the emoji proposed here are
original ideas; they are just variants of existing ones that complete the set of explicitly gendered
emoji that has been steadily growing since Unicode 9. If the 184 gendered emoji that exist in
Unicode today have been approved, there is absolutely no reason to reject any of the 35 suggestions
in this document. Any argument against them can only result from personal prejudice and biases.

The enormous collection of gendered emoji was not added because users strictly wanted them, but
because the UTC felt that women were unfairly represented in the set at the time. This could have
easily been fixed if vendors had employed some simple glyph changes, but the UTC opted to make
gender an inherent, fundamental property of emoji instead. Yes, there were calls for a female runner
or a female police officer � I am not denying that �, but there most definitely was no reason for
three distinct flavours of U+1F6A3 ROWBOAT.

For some gendered emoji it's not even possible to track down proper proposals. MOTHER CHRISTMAS
for instance was first vaguely discussed in L2/15-048 (Parrott, `Adding gender counterparts to
emoji list?'), suddenly reappeared in L2/15-054R5 (ESC, `Emoji Additions: Animals, Compatibility,
and More Popular Requests') as a recommendation to the UTC, and was then swiftly encoded one
year later as U+1F936 in Unicode 9. No evidence for the potential popularity or usage level of this
character was ever provided; at least my search did not reveal any publicly available documents
with this information.

The instructions for emoji proposals state that emoji will not be accepted just because they further a
cause but only despite of it (if approved at all). Luckily for the authors of L2/16-160 (`Expanding
Emoji Professions: Reducing Gender Inequality') this disclaimer was written after most of the
gendered emoji had already been formally added to Unicode. I have seen no official admissions by
members of the Unicode Consortium that Emoji 4.0 was a mistake in retrospect, so I have no choice
but to assume that the same criteria and processes that led to `man with bunny ears partying' also
still apply to the emoji I propose in this document. I am not asking the UTC to accept any emoji on
blind faith without justification; I am asking the UTC to be consistent in their own actions. I am
asking the UTC to treat all people as equal, whether their existence aligns with individual members'
personal views or not. If MOTHER CHRISTMAS can be added because she appears in a handful of
Christmas stories then Unicode has no excuse to reject emoji that represent real identities of real
people in the real world. If it can be unanimously agreed that fairies, zombies, and vampires deserve
proper gender representation right from the get-go then transgender people should not have to be
begging on their knees for months to receive the same treatment. The longer one thinks about the
current Unicode gender situation the more ridiculous and insulting it becomes.

And again, I am not advocating for representations of each and every minuscule aspect of human
nature in plain text. I merely want the UTC to actually respect those representations that they
themselves claim to care about, and in the case of gender this means distinct options for male,
female, and neutral. If this proposal will not be accepted then I request the UTC to cease adding any
gender variants for any new emoji in the future, as well as formally deprecating all gender variants

                                                          9/20
                                                                                                                                  Proposal for Fully Gender-Inclusive Emoji

added in the past. You cannot have it both ways.
Nevertheless, here are various Twitter users expressing their discontent with the way emoji and
gender currently interact. While some of the frustration is directed at specific implementations and
not directly at Unicode, said implementations ultimately just are a result of official Unicode
documentation. Previously gender-inclusive fonts like Noto Color Emoji were changed to be
explicitly gendered because Unicode recommends fixed genders for many emoji, and default glyphs
aren't implemented as neutral because Unicode treats the neutral option as second-class to male and
female, even going so far as calling it "typical duplicates" in tallies, so vendors see no need for a
third gender.

                                                         10/20
                                            Proposal for Fully Gender-Inclusive Emoji

11/20
                                            Proposal for Fully Gender-Inclusive Emoji

12/20
                                            Proposal for Fully Gender-Inclusive Emoji

13/20
                                                                                                                                  Proposal for Fully Gender-Inclusive Emoji

Not only do people want to use gender combinations that currently are not possible under
Emoji 5.0, they also want to include emoji in their messages that don't specify gender at all, which
only becomes feasible once neutral variants of all humans are widely available, which in turn can
only realistically happen if more explicitly neutral emoji than just ADULT, CHILD, and OLDER ADULT
exist. It makes no sense to assign a gender to an abstract gesture or emotion unless you are talking
about a specific person and somehow that person's gender is relevant to the topic at hand.
Emoji always have the same meaning regardless of their gender display. It is expected that the
emoji proposed here will be used in exactly the same way as their already existing counterparts, and
I see no reason why these new emoji wouldn't be used with a similar frequency to the old ones once
they become widely supported by fonts and keyboards. The usefulness of all emoji that this
proposal wishes to modify and expand upon has already been proven by various individual
proposals in the past.
C. Image distinctiveness
There are hardly any visible differences between gender-specific versions of the same emoji,
especially at standard display sizes. The emoji proposed here are sadly no exception to that, as this
is an unavoidable problem when trying to represent something non-visual like gender in a purely
visual medium. Vendors can easily reuse their designs for ADULT, MAN, and WOMAN and apply

                                                         14/20
                                                                                                                                  Proposal for Fully Gender-Inclusive Emoji

different accessories to form the missing glyphs.

D. Completeness
The overview table in section 2 should have made it quite obvious that Emoji 5.0 is riddled with
inexplicable holes.

    � 46 concepts are available as three genders
    � 19 concepts are available as only two genders
    � 8 concepts are available as just one single gender

6 of those 27 restricted emoji are compatibility characters from the original Japanese carrier emoji
sets and Wingdings/Webdings. However, 29 of the 46 fully-inclusive emoji also originate from
those sources so it cannot be argued that the variants proposed here are any less important or urgent
than those already encoded. All emoji I propose show normal, regular people whereas the existing
Unicode gender pairs also include simple gestures (HAPPY PERSON RAISING ONE HAND, SHRUG, FACE
PALM etc.) and, strangely enough, what essentially amounts to inanimate objects (ROWBOAT).

E. Frequently Requested
This is a difficult point to address because we are essentially dealing with a niche audience here.
Everybody knows what a carrot or a butterfly is but many people are completely unaware of the
existence of non-binary genders or even the entire concept of transgender, especially in the West.
Knowledge of the significance of a moon cake for instance is also limited to a very specific group,
but this group at least makes up a considerable percentage of the world population. It is estimated
that up to 0.6% of United States citizens are transgender. If we extrapolate this number we get
roughly 45 million transgender people worldwide, and the amount of non-binary people is lower
than that still. Meanwhile, the recently approved Nazar is a frequent sight in at least eighteen
different countries, one of them the second-most popular nation India.

The search for requests is made even more difficult by the fact that, as mentioned previously, all the
emoji proposed here already exist, just with different genders. Of course, I did find numerous
examples of people requesting better gender representation on Twitter and included a selection of
tweets above. Furthermore, reactions to the approval of ADULT and co. showed that many people
welcome the addition of gender-neutral emoji. I am sure that those same people would also like to
see the third gender option be expanded to more than just generic, featureless people. I could not
find any specific expressions of these wishes anywhere else, though. I also suspect that I am the
only person who has been pestering the UTC regularly for improvements. Let's just say that the set
(cares about gender)  (cares about emoji)  (knows that Unicode makes emoji) is quite small.

That being said, I believe that this factor is another one that cannot be handled in the usual way for
this proposal. Seeing how the vast majority of the Emoji 4.0 additions came to be despite a
complete lack of visible public support, it would only be fair to give this proposal a bit more leeway
as well. Besides, I am certain that I have already shown more user requests for `pregnant man' than
`man gesturing no' could ever hope to gather.

5. Factors for Exclusion

F. Overly Specific
While I personally think that having any gender options at all is too overly specific, the Unicode
Consortium evidently does not agree with me. Three has been agreed upon by the UTC as the
number of necessary genders.

                                                         15/20
                                                                                                                                  Proposal for Fully Gender-Inclusive Emoji

G. Open-ended
The number of gender variants per emoji will always remain three because the neutral option is
intended to encompass everything that is not 100% male or 100% female. There are presently no
plans to propose distinct gender options for different non-binary genders, or to differentiate non-
binary genders from the absence of gender.

The UTC must keep in mind that all future human-form emoji additions need to be equipped with
the full range of gender options as soon as they are released. As stated in the past, this only applies
for characters that represent people who are old enough to know their gender, i.e. not infants.

H. Already Representable
With the exception of the three emoji proposed as atomic codepoints, all emoji listed in this
document are sequences of already existing Unicode characters. However, all major emoji vendors
have so far respected the canonical list of human-form ZWJ sequences and do not support any of
the missing variations. Therefore they all need to be added to the emoji data so that vendors will
implement them.

I. Logos, Brands etc.
Not applicable.

J. Transient
Humans have assigned genders to themselves for millennia. Despite widespread belief otherwise,
non-binary genders are not a recent invention but have also existed in some way or form for just as
long in several unrelated cultures all around the world, for example the Zuni, the Lakota, the
Mohave, the Zapotec, the Navajo, the Bugis, Native Hawaiians, Samoans, Tongans, as well as
various other peoples on the Indian subcontinent, in Africa, and in the Middle East, to just name a
few.

In Western culture, the number of openly transgender and non-binary people will only increase in
the future as being trans becomes more acceptable in society � albeit very slowly � and as broader
ranges of the population become aware of new, more accurate scientific theories of gender that
supersede those ancient schools of thought which cannot reasonably describe human nature, giving
more closeted people the opportunity to come out more safely. People are also increasingly
rejecting the archaic binary model of gender and care less and less about old stereotypes and
traditional societal roles, regardless of their own gender identity. All of this means that more and
more people will be using genderless emoji and emoji that break with common tropes as time goes
on.

K. Faulty Comparison
All gendered variants � whether already existent or not � are equally important, which is why none
must be excluded. If the UTC cannot agree that this statement is true, thereby implying that some
genders are more important than others � that some humans are more important than others � then
they must also admit that Emoji 4.0 was released in error and should never have existed.

6. Sort Location

The standard sort order for existing gendered emoji is neutral < male < female. The
proposed set simply fills all gaps following this pattern.

                                                         16/20
                                                                                                                                  Proposal for Fully Gender-Inclusive Emoji

7. Other Information

The only way to differentiate genders in emoji is by employing exaggerated stereotypes, e.g. hair
length, face shape, and breast size. Some of the proposed emoji may therefore be hard to design for
vendors because they don't always show any visible hair or breasts. For the general user who may
care about selecting the "correct" gender this can lead to small issues, although the fixed order of
gender sets on keyboards should make it obvious which is which nonetheless. More detailed fonts
like Apple Color Emoji or the native Facebook set are inherently better suited to display these subtle
characteristics.

The largest contrast within an existing gender pair occurs between DANCER and MAN DANCING,
which might as well be two completely unrelated emoji as it stands now. For the PERSON DANCING
sample glyph in this proposal I have chosen DANCER's style because it is more iconic and
expressive. It may be advisable to also adapt MAN DANCING to look more similar to DANCER once
PERSON DANCING has been added so that users can more easily recognize the connection.

For the majority of this document I have been talking about non-binary people, or "enbies", as if
they were some homogeneous mass. Obviously reality is far too complicated to be described in a
minutely accurate manner in just a few thousand words, and it is definitely too complicated for a
character encoding standard. Some non-binary genders are in an intermediate state between male
and female, some are wholly separate from that spectrum. Some people have several genders at
once, some have none at all, and some change their gender from time to time or based on their
surroundings. Some have conscious control over their gender while others don't. Some gender
concepts from around the world can't be translated at all to our Western society in a way that's
immediately comprehensible, which is why it becomes questionable whether Unicode's three-
gender model can ever truly represent gender at all. What gender entails and what it means varies
immensely from culture to culture and from person to person. Human gender is unbelievably
complex and I am not in the slightest qualified to talk about it in any more detail than that, but I will
try to supply additional educational material should the UTC see the need.

This document also serves as your periodic reminder that gender is not in any way related to
physical biology. Men can breast-feed, even cisgender men can breast-feed. In fact, mammary
glands are the defining feature of all mammals. If you think that men cannot get pregnant, I would
like to introduce you to Thomas Beatie (https://en.wikipedia.org/wiki/Thomas_Beatie), just one of
many counter-examples. If you think that cis men cannot get pregnant, then you will surely
appreciate the case of "Rob", a man who identifies as male, was assigned male at birth, has a penis
and testicles, but also possesses a fully functional uterus which would allow him to bear a child
(http://www.cosmopolitan.com/lifestyle/news/a36344/man-discovers-he-has-a-working-womb-and-
uterus/).

Furthermore, the fact that anyone can wear any clothes regardless of their gender is probably not
even worth mentioning at this point. Clothes do not have gender; people do.

It is incredibly sad that emoji vendors are forced to represent such a colourful aspect of the human
condition in simplified, abstracted pictographs that didn't need it in the first place. Gender has
nothing to do with physiology or clothing or hair style or make-up, but tragically those are the only
ways to tell the difference between men, women, and enbies so that a mass audience as broad as the
entire population of Earth can understand it at a glance.

                                                         17/20
                                                                                                                                  Proposal for Fully Gender-Inclusive Emoji

If there is one piece of advice I can give to emoji vendors when it comes to gender display it's the
following:

        Don't try.

Nothing purely visual you can come up with will ever even scratch the surface of acceptable gender
representation, believe me. Simply display all gender variants of the same emoji identically to each
other if you can. Discard any `' and `' you come across. Use the same glyph for DANCER as
for MAN DANCING and PERSON DANCING. You cannot win at this.

8. Images

Note that some of the proposed emoji will initially look identical to existing ones because all
human-form emoji as of now are either explicitly gendered or look gendered despite not being
supposed to.

The 35 sample glyphs included in this proposal have been adapted from Twemoji
(https://github.com/twitter/twemoji), a free and open-source emoji set created by Twitter, inc. (List
of contributors: https://github.com/twitter/twemoji/graphs/contributors). Twemoji graphics are
licensed under CC-BY 4.0 (https://creativecommons.org/licenses/by/4.0/), which means they can be
altered and redistributed for commercial and non-commercial purposes as long as the original
creator is properly attributed and no additional legal or technical restrictions have been applied to
the material.

Most files have been manipulated to create alternate male/female/neutral versions by switching out
facial features and hair dues. The following emoji were left untouched:

    � man with Chinese cap
    � woman with veil
    � man in tuxedo
    � man in suit levitating
    � pregnant woman
    � woman breast-feeding
    � woman with headscarf
    � bearded person

9. References

� Wikipedia. "Transgender". https://en.wikipedia.org/wiki/Transgender
     Parsons, Elsie Clews (1916). "The Zu�i La'mana". American Anthropologist. American
         Anthropological Association. 18 (4): 521�8.
     Sch�tzer, M.A.N. (1994). "Winyanktehca: Two-souls person".
     Parker, H.N. (2001). "The myth of the heterosexual: anthropology and sexuality for
         classicists", from Arethusa 0004-0975, vol 34, p:313, 2001.
     Stephen, Lynn (2002). "Sexualities and Genders in Zapotec Oaxaca". Latin American
         Perspectives. Sage Publications, Inc. 29 (2): 41�59.

� Wikipedia. "Third gender". https://en.wikipedia.org/wiki/Third_gender
     Estrada, Gabriel S (2011). "Two Spirits, N�dleeh, and LGBTQ2 Navajo Gaze". American
         Indian Culture and Research Journal. 35 (4): 167�190.

� Wikipedia. "Gender in Bugis society". https://en.wikipedia.org/wiki/Gender_in_Bugis_society

                                                         18/20
                                                                                                                                  Proposal for Fully Gender-Inclusive Emoji

� Wikipedia. "Mh". https://en.wikipedia.org/wiki/M%C4%81h%C5%AB
� Wikipedia. "Fakaleiti". https://en.wikipedia.org/wiki/Fakaleiti
� Wikipedia. "Faafafine". https://en.wikipedia.org/wiki/Fa%27afafine
� Wikipedia. "Genderqueer". https://en.wikipedia.org/wiki/Genderqueer

Documents discussed:

� Charlotte Buff. "Comment on Document L2/16-160 Concerning Emoji Gender Pairs for
    Professions" (http://www.unicode.org/L2/L2016/16169-gendered-prof-cmt.pdf)

� Charlotte Buff. "Another Comment on Gendered Emoji"
    (http://www.unicode.org/L2/L2016/16193-gendered-emoji-2.pdf)

� Paul D. Hunt. "Proposal to enable inclusive emoji representation"
    (http://www.unicode.org/L2/L2016/16317-gender-inclusive-emoji.pdf)

� Mark Davis et al. "Gender-Neutral Human form Emoji"
    (http://www.unicode.org/L2/L2017/17071-gender-neutral-humanform.pdf)

� Katrina Parrott et al. "Adding gender counterparts to emoji list?"
    (http://www.unicode.org/L2/L2015/15048-gender-cntrprt.pdf)

� Emoji Sub-committee. "Emoji Additions: Animals, Compatibility, and More Popular Requests
    (http://www.unicode.org/L2/L2015/15054r5-emoji-tranche5.pdf)

� Rachel Been et al. "Expanding Emoji Professions: Reducing Gender Inequality"
    (http://www.unicode.org/L2/L2016/16160-emoji-professions.pdf)

As far as I know, the following documents never reached the UTC but were only discussed with the
document registrar and the Emoji Subcommittee:
� Charlotte Buff. "The Fourth Comment on Gendered Emoji" (http://share.randomguy32.de/esc-

    doc/gendered-emoji-yet-again.pdf)
� Charlotte Buff. "Filling the Gaps in the Emoji 5.0 Repertoire"

    (http://share.randomguy32.de/esc-doc/gendered-emoji-proposal-only.pdf)
� Charlotte Buff. "Revised Proposal to Fill the Gaps in the Emoji 5.0 Repertoire"

    (http://share.randomguy32.de/esc-doc/gendered-emoji-proposal-only-new.pdf)
� Charlotte Buff. "Response to Feedback on My Latest Proposal"

    (http://share.randomguy32.de/esc-doc/gendered-emoji-response.pdf)
� Charlotte Buff. "Request for Clarification of Gendered Emoji Situation"

    (http://share.randomguy32.de/esc-doc/gendered-emoji-enquiry.pdf)

Tweets used:

� https://twitter.com/ASquad/status/856171328105324546
� https://twitter.com/ChildishShamiro/status/877920161474334720
� https://twitter.com/CostcoBlack/status/868287538703863809
� https://twitter.com/GlitchyCat/status/867939425379991552
� https://twitter.com/Humanberg/status/866021403803430912
� https://twitter.com/Iodeddiper/status/864442156362149889
� https://twitter.com/ItsBooshie/status/877593641111257088
� https://twitter.com/Lunatoons25/status/863270259972812801
� https://twitter.com/MichalBryxi/status/868213654650580994
� https://twitter.com/Nicali4444/status/870125374134513665
� https://twitter.com/Opaopa13/status/865601163009327106
� https://twitter.com/RvLeshrac/status/843267542001049600
� https://twitter.com/SamirTalwar/status/868043059883323392

                                                         19/20
                                                                                                                                  Proposal for Fully Gender-Inclusive Emoji

� https://twitter.com/TonyMilano43/status/867049782853947394
� https://twitter.com/Zac_coolprous/status/871388753687871488
� https://twitter.com/adargueta/status/862500886895112192
� https://twitter.com/bryan_martin/status/837141233126486016
� https://twitter.com/chaleurhumaines/status/864046600762658816
� https://twitter.com/charade_s/status/855317241809612801
� https://twitter.com/chordbug/status/861341480891420675
� https://twitter.com/drejp55/status/841752905157902336
� https://twitter.com/eevee/status/865109857615073281
� https://twitter.com/fear_the_man/status/877120639546642432
� https://twitter.com/freezydorito/status/864909327026581504
� https://twitter.com/freezydorito/status/872753018399318016
� https://twitter.com/furt1v3ly/status/849480548695384064
� https://twitter.com/ialexi/status/807280566890434560
� https://twitter.com/krizpp/status/850846327042969601
� https://twitter.com/longisland_mom/status/844739133306167296
� https://twitter.com/modgethanc/status/848886531750334464
� https://twitter.com/so_it_gohs/status/877944539578736640
� https://twitter.com/studmuffin4cm/status/868678616925716480
� https://twitter.com/tallshmo/status/854482468224761861
� https://twitter.com/vermicelli/status/833725990966853632

                                                         20/20

```
