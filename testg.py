def find_consecutive_repeated_dialogs(file_path, encoding='utf-8'):
    # Read the content of the file
    with open(file_path, 'r', encoding=encoding) as file:
        lines = file.readlines()
    
    previous_dialog = None
    previous_char_name = None
    dial=None
    cl=[]
    wasClaudia=False
    isClaudia=False
    for i in range(0, len(lines)):
        # Split the lines into character name and dialog
        char_name_2, dialog_2 = lines[i].strip().split('\t', 1)
        if char_name_2=="CLAUDIA":
            print(str(i)+" "+lines[i])
            print("is claudia")
            if wasClaudia:
                print("add")
                dial=dial+dialog_2
            else:
                print("new")
                dial=dialog_2
                wasClaudia=True
        else:
            print("flush")
            if len(dial)>0:
                cl.append(dial)
            dial=""
            wasClaudia=False
    cl.append(dial)
    for k in cl:
        print("CLAUDIA\t"+str(k))         
# Example usage
file_path = 'dialogs.txt'  # Path to your text file
encoding = 'utf-8'  # Encoding of the text file

# Example content
example_text = """CLAUDIA	I felt like I’d been under there my
CLAUDIA	entire life. Wrapped in yellow
CLAUDIA	blankets, like a baby, swaddled too
CLAUDIA	tight. I was sinking, further and
CLAUDIA	further, and just when I was about
CLAUDIA	to run out of breath... something
CLAUDIA	pulled me out. Something in the
CLAUDIA	trees. A light. A glow.
CLAUDIA	Is someone thirsty?
GRACE	Hello? Anyone there?
GRACE	Hello...
GRACE	Tilly! Hi!
GRACE	Where are you off to?
GRACE	Hey...
GRACE	Hey... it’s okay...
GRACE	Your dog’s really cute...
CLAUDIA	Don’t take her.
GRACE	I just wanted to make sure you’re
GRACE	okay...
GRACE	Are you... okay?
CLAUDIA	How did you know I was here?
GRACE	Well... I was there. Last night, at
GRACE	the reservoir.
GRACE	I saw what happened.
GRACE	I won’t tell anyone, I pinky
GRACE	promise.
CLAUDIA	What are you doing with your
CLAUDIA	finger?
GRACE	Haven’t you heard of a pinky
GRACE	promise?
GRACE	Well, it means more than a normal
GRACE	handshake.
GRACE	So... what’s your name?
CLAUDIA	Claudia.
GRACE	I’m Grace.
CLAUDIA	What colour are the other fingers?
CLAUDIA	If this one is pink, what colour
CLAUDIA	are the others?
GRACE	Well it’s not that the finger is
GRACE	pink... it’s just called the pinky
GRACE	finger. The other ones all have
GRACE	different names. You know them,
GRACE	right?
CLAUDIA	First, second, third-
GRACE	Uh, uh.
GRACE	Pinky, ring, rude...
CLAUDIA	What makes it rude?
CLAUDIA	What?
GRACE	Don’t do that!
GRACE	It’s like saying something really
GRACE	mean, but with your finger.
GRACE	Do you want to sit with me?
GRACE	Can I come back and visit you
GRACE	sometime?
CLAUDIA	No one can know I’m here. If they
CLAUDIA	find out they’ll take me away.
GRACE	I won’t tell anyone.
GRACE	It can be our secret.
CLAUDIA	Purple promise?
GRACE	Purple promise.
CLAUDIA	It was her. Grace. The glow on the
CLAUDIA	bank...
CLAUDIA	The pull from the trees.
CLAUDIA	She is not of this place.
CROYDON	Don’t worry, mate. She’s not in any
CROYDON	trouble.
MIKE	That’d be a fuckin’ first.
DONNA	Do you want me to have a nervous
DONNA	breakdown, Grace, is that it?
GRACE	No, mum.
DONNA	Then why the fuck are the cops
DONNA	here?
GRACE	I dunno...
DONNA	What the fuck have you been up to?
GRACE	I haven’t done a fucking thing.
MIKE	Hey, hey... Don’t talk to your
MIKE	mother like that.
CROYDON	We just need to ask her a few more
CROYDON	questions, okay?
CROYDON	Okay, so... I’m Detective Croydon
CROYDON	and this is my partner, Detective
CROYDON	Jones.
CROYDON	We just wanted to clarify what you
CROYDON	saw at the Res last night.
JONES	You said you saw some thrashing in
JONES	the water, and then you said you
JONES	saw a girl running away from the
JONES	Res... and we’re not sure who that
JONES	is.
CROYDON	See, the deceased didn’t have any
CROYDON	kids or family, so we think it
CROYDON	must’ve been a visitor or someone
CROYDON	from out of town.
CROYDON	Is there anything you can tell us
CROYDON	about-
GRACE	Look.
JONES	We really need you to think-
GRACE	It’s a scorpion in a lollipop.
JONES	What did she look like?
JONES	Light hair, dark hair?
GRACE	Yeah, look, I don’t really think I
GRACE	saw a girl.
JONES	No girl...
GRACE	No. It was dark and I was on my own
GRACE	and I think I got freaked and saw
GRACE	things that weren’t actually there.
GRACE	I’ve got a really overactive
GRACE	imagination. Mum says it all the
GRACE	time.
CROYDON	So wait, let me get this
CROYDON	straight... There was no girl.
JONES	But you did say-
GRACE	Yeah I know, I know. But I’m saying
GRACE	I think I got carried away when I
GRACE	was speaking to the officer last
GRACE	night. There was no girl.
GRACE	But I did see a woman, an older
GRACE	lady, walking into the water. And
GRACE	then the thrashing.
CROYDON	Right. So, you saw an older woman
CROYDON	walking into the water-
GRACE	Yeah, that author lady who lives by
GRACE	the Res. I recognised her from the
GRACE	back of one of her books.
CROYDON	Veronica Fox?
GRACE	Yeah, that’s her. She just walked
GRACE	into the water and didn’t come out.
GRACE	It was fucked.
CROYDON	Well, sounds about right.
GRACE	Cool.
GRACE	So I’m good? I’m not in trouble?
CROYDON	You’re not in trouble. Like I said,
CROYDON	we just wanted to clarify a few
CROYDON	things.
JONES	You’ve been a big help, thank you,
JONES	Grace.
JONES	Hey... what you saw must’ve been
JONES	really scary. You got someone you
JONES	can talk to about it, if you need
JONES	to?
VERONICA	Lessons, my darling.
VERONICA	Claudia, what’s the matter?
CLAUDIA	I don’t know.
VERONICA	Are you having bad thoughts again?
VERONICA	Sweetheart.
VERONICA	Deep breaths, baby.
VERONICA	Breathe with me, okay?
GRACE	In... and out...
GRACE	Hey, it’s okay, it’s me.
CLAUDIA	Where did my mum go?
CLAUDIA	How did you get in here?
GRACE	The door was open... I knocked but-
CLAUDIA	Who else is here?
GRACE	No one, I-
CLAUDIA	I feel sick.
CLAUDIA	I don’t feel good.
CLAUDIA	I don’t feel good! I don’t feel
CLAUDIA	good!
GRACE	I’m here. I’m going to put my hand
GRACE	on your back, okay?
CLAUDIA	What have I done?
CLAUDIA	What did I do?
GRACE	Let’s get some air, okay?
CLAUDIA	What did I do to her?!
GRACE	Hey, hey, come here.
CLAUDIA	I should be with her!
GRACE	Look at me.
GRACE	Claudia, hey!
CLAUDIA	I need to go back. I need to be
CLAUDIA	with her. I-
GRACE	Don’t say that.
GRACE	Shit.
GRACE	Claudia?
GRACE	CLAUDIA?
GRACE	CLAUDIA?!
GRACE	Hey...
GRACE	Claudia?
CLAUDIA	I should be with her.
CLAUDIA	I should be with her.
GRACE	You can’t be seen here...
GRACE	You don’t want to be found, do you?
GRACE	Hey... let’s go home, yeah?
GRACE	Let me take you home where it’s
GRACE	safe.
GRACE	Can I wash your hair?
GRACE	I’m going to touch your head, okay?
GRACE	You have to look in the mirror.
CLAUDIA	Why?
GRACE	Just look.
CLAUDIA	What?
GRACE	Nothing.
CLAUDIA	Can I do you?
GRACE	My hair’s too long; it wouldn’t
GRACE	stay.
CLAUDIA	Get in.
CLAUDIA	What are you doing?
CLAUDIA	You wear clothes in the bath?
GRACE	No. Not normally.
CLAUDIA	Okay, dunk your head.
GRACE	Do you like it here?
CLAUDIA	In the tub?
GRACE	No, I mean... this house.
CLAUDIA	I guess.
GRACE	Why don’t you ever leave?
CLAUDIA	I’ve left before.
GRACE	I don’t think the Res counts.
CLAUDIA	It’s on the outside...
GRACE	I know, but I mean, the real
GRACE	outside.
CLAUDIA	Mum said that there’s nothing but
CLAUDIA	pain there.
GRACE	Your mum said that?
CLAUDIA	She came from there. She said that
CLAUDIA	it’s filled with selfish people who
CLAUDIA	don’t treat each other very well.
GRACE	So you’ve really never been past
GRACE	the Res?
CLAUDIA	Why would I?
GRACE	I don’t know... to go to school...
GRACE	see a doctor... go to your
GRACE	grandparents houses and have cups
GRACE	of tea and listen to the same
GRACE	boring story ten times over.
GRACE	I mean, I can’t believe it...
CLAUDIA	Why are you laughing?
GRACE	So no one knows you exist...
CLAUDIA	You do.
CLAUDIA	You can look in the mirror now.
GRACE	You’re very good at this.
CLAUDIA	Yeah.
GRACE	I’ve never read any of your mum’s
GRACE	books.
GRACE	I hear they’re really depressing.
CLAUDIA	I’m not allowed to read them until
CLAUDIA	I turn 18.
GRACE	How old are you now?
CLAUDIA	16.
GRACE	Same.
GRACE	“Lord, how unutterably disgusting
GRACE	life is! What dirty tricks it plays
GRACE	us, one moment free; the next,
GRACE	this. Here we are among the
GRACE	breadcrumbs and the stained napkins
GRACE	again. That knife is already
GRACE	congealing with grease. Disorder,
GRACE	sordidity and corruption surrounds
GRACE	us. We have been taking into our
GRACE	mouths the bodies of dead birds. It
GRACE	is with these greasy crumbs,
GRACE	slobbering over napkins, and little
GRACE	corpses that we have to build.
GRACE	Always it begins again; always
GRACE	there is the enemy; eyes meeting
GRACE	ours; fingers twitching ours; the
GRACE	effort waiting. Call the waiter.
GRACE	Pay the bill. We must pull
GRACE	ourselves up out of the chairs. We
GRACE	must find our coats. We must go.
GRACE	Must, must, must — detestable word.
GRACE	Once more, I who had thought myself
GRACE	immune, who had said, "Now I am rid
GRACE	of all that", find that the wave
GRACE	has tumbled me over, head over
GRACE	heels, scattering my possessions,
GRACE	leaving me to collect, to assemble,
GRACE	to head together, to summon my
GRACE	forces, rise and confront the
GRACE	enemy.”
GRACE	Why was that page marked?
CLAUDIA	Mum was showing it to me in class.
GRACE	Wow.
CLAUDIA	What?
GRACE	I thought that my mum was fucked.
GRACE	I’m sorry. I shouldn’t have said
GRACE	that.
CLAUDIA	Mum just felt everybody’s pain. But
CLAUDIA	she’s free now.
CLAUDIA	What’s your mum like?
GRACE	She’s the worst.
CLAUDIA	Why?
GRACE	I shouldn’t say that. She just has
GRACE	a lot of problems.
GRACE	And her boyfriend’s a dick. It’s
GRACE	nice to be away from it, to be
GRACE	honest.
GRACE	I like spending time with you here.
CLAUDIA	Pointer, rude, ring... pinky.
MIKE	Hey, sweetie.
MIKE	You should come inside. Mozzies are
MIKE	out in force tonight.
GRACE	I’m okay.
MIKE	Fair enough. It’s a nice night.
MIKE	Where you been?
GRACE	Friend’s place.
MIKE	Our secret.
MIKE	A friend, ay? Boyfriend?
MIKE	My little girl all grown up.
GRACE	I’m not your little girl, Mike.
MIKE	Hey, don’t be like that.
MIKE	So, do you have a boyfriend?
MIKE	It’s okay if you do. So long as
MIKE	you’re using protection-
MIKE	Hey, come on. I’m only playin’.
GRACE	Goodnight, Mike.
MIKE	Night.
GRACE	I have no idea what I packed - I
GRACE	just grabbed whatever I could
GRACE	before mum woke up.
CLAUDIA	What’s that?
GRACE	Strawberry milk. Want some?
CLAUDIA	Strawberry milk?
GRACE	It’s really good.
GRACE	You’ll love it. I purple promise.
GRACE	Don’t choke!
GRACE	Guess what else I brought.
CLAUDIA	A treasure chest.
GRACE	Kinda.
CLAUDIA	My mother said the fences are the
CLAUDIA	walls of her womb. Said she could
CLAUDIA	only protect me if I stayed inside,
CLAUDIA	away from everyone, everything.
GRACE	I made these.
GRACE	I’m gonna sell them at a market.
GRACE	These are my ticket out of here.
CLAUDIA	Where do you want to go?
GRACE	Somewhere. Anywhere.
GRACE	Do you like them?
CLAUDIA	They’re very... Colourful.
GRACE	These are my favourites... “Brave”
GRACE	and “Badass”.
GRACE	Okay... So...
GRACE	Tell me something you like about
GRACE	yourself.
GRACE	Okay, I’ll tell you something I
GRACE	like about you.
CLAUDIA	You hardly know me.
GRACE	I know enough...
CLAUDIA	Smart?
GRACE	Aren’t you?
CLAUDIA	What else?
CLAUDIA	Am I pretty?
GRACE	Choose your favourite colours from
GRACE	that pile.
GRACE	Which ones do you like the best?
CLAUDIA	I don’t know...
CLAUDIA	I think I like this one.
GRACE	Turquoise.
CLAUDIA	Turquoise. I like turquoise.
GRACE	Me too.
GRACE	You’re a natural. Maybe you can
GRACE	help me make some for the market.
GRACE	Is there a ladder into this thing?
CLAUDIA	Why?
GRACE	It’s two hundred thousand degrees.
GRACE	My body needs to be wet,
GRACE	immediately.
CLAUDIA	The dam’s just through those
CLAUDIA	trees...
GRACE	Where?
GRACE	Are you okay?
CLAUDIA	Yeah... I just keep having these...
CLAUDIA	I don’t really like water. Apart
CLAUDIA	from baths, I mean.
GRACE	Best way to overcome a fear is to
GRACE	confront it.
GRACE	Seriously, I heard it on the TV and
GRACE	everything.
CLAUDIA	Hey!
GRACE	You can’t tell me that didn’t feel
GRACE	good.
CLAUDIA	No!
GRACE	Come on!
GRACE	Victory!
CLAUDIA	How deep is it?
CLAUDIA	Wait!
GRACE	What?
CLAUDIA	My jewels...
GRACE	They’re waterproof, look.
GRACE	Ready to go under?
GRACE	Hey, hey... Look at me.
GRACE	Breathe with me, okay?
GRACE	In... and out...
CLAUDIA	My mum used to do that for me.
GRACE	Trust me.
GRACE	Nice, right?
GRACE	Are you ready?
CLAUDIA	I’m scared.
GRACE	That’s okay. It’s okay to be
GRACE	scared.
GRACE	Just keep looking at me, Okay?
GRACE	Three, two...
GRACE	Lucky charm!
GRACE	Here, you have it.
CLAUDIA	Can you still eat it?
GRACE	Yeah!
GRACE	Feel lucky?
CLAUDIA	Yeah.
GRACE	Are you okay?
CLAUDIA	I don’t know how I’m supposed to be
CLAUDIA	feeling.
CLAUDIA	You make me think that all the
CLAUDIA	stuff my mum taught me in class -
CLAUDIA	about the world being cruel and
CLAUDIA	people being monsters - is a lie.
GRACE	How do you know I’m not a monster?
CLAUDIA	Do you think you are?
GRACE	Not many people like me.
CLAUDIA	Because monsters only like other
CLAUDIA	monsters.
CLAUDIA	Welcome!
CLAUDIA	Okay, I’ve found it.
CLAUDIA	‘When Day is Over’ by Lesbia
CLAUDIA	Harford. Ready?
GRACE	Yeah.
CLAUDIA	When day is over
CLAUDIA	I climb up the stair,
CLAUDIA	Take off my dark dress,
CLAUDIA	Pull down my hair,
CLAUDIA	Open my window
CLAUDIA	And look at the stars.
CLAUDIA	Then my heart breaks through
CLAUDIA	These prison bars
CLAUDIA	Of space and darkness
CLAUDIA	And finds what is true,
CLAUDIA	Up past the stars where
CLAUDIA	I'm one with you.
GRACE	Come and sit with me.
GRACE	I like the image of your heart
GRACE	breaking through prison bars.
GRACE	Can I feel it?
CLAUDIA	Feel what?
GRACE	Your heart?
CLAUDIA	Can you hear it?
GRACE	Yes.
CLAUDIA	Is it okay?
GRACE	Yes.
CLAUDIA	It should be broken, shouldn’t it.
GRACE	Shock can make you numb.
CLAUDIA	I don’t feel numb.
GRACE	What do you feel?
CLAUDIA	I feel more alive than I’ve ever
CLAUDIA	felt.
CLAUDIA	I’m sorry. I shouldn’t have said
CLAUDIA	that.
GRACE	No! It’s okay! I-
CLAUDIA	Maybe you should go.
GRACE	What?
CLAUDIA	I need you to go.
GRACE	Claudia...
CLAUDIA	I need you to go and I need you not
CLAUDIA	to come back.
CLAUDIA	Go.
CLAUDIA	GO!
CLAUDIA	My mother said there would come a
CLAUDIA	time when we would have to leave.
CLAUDIA	We talked about it for months.
CLAUDIA	About how we would be light again,
CLAUDIA	without pain. But when the time
CLAUDIA	came, I couldn’t do it. I left her
CLAUDIA	sinking, further and further and
CLAUDIA	further.
DONNA	What the fuck’re you doin’ in
DONNA	there? Tryin’ to sleep!
CLAUDIA	Grace?
JONES	Hey, hey, who’s this?
JONES	There’s a dog here.
JONES	Hey buddy... what’s your name?
CLAUDIA	Tilly... No.
JONES	Aren’t you a beautiful girl, huh?
JONES	See, told you it was worth a look.
CROYDON	Put her in the car and I’ll give
CROYDON	the place a once-over.
JONES	On it. Come on, Tilly!
CROYDON	“Diving Into Concrete”...
JONES	What’s that?
CROYDON	A signed copy of one of her books.
CROYDON	Should fetch a pretty penny.
JONES	I’ll tell Sarge.
JONES	Wait, who’s it addressed to?
CROYDON	What? Why?
JONES	Well, why would she keep a signed
JONES	copy of her own book?
CROYDON	“My darling Claudia, I love you
CROYDON	more than anything. You are my
CROYDON	world.”
JONES	Maybe this isn’t just another local
JONES	killing herself from boredom?
CROYDON	A murder investigation, ay?
JONES	Never know. Could be a lead.
CROYDON	Doubt it. Sounds too interesting
CROYDON	for this shit hole town.
JONES	Where are you off to?
GRACE	I was just-
CROYDON	I thought I told you to steer clear
CROYDON	of the Res.
GRACE	Tilly?!
CROYDON	You know this dog?
GRACE	I’ve been out looking for her all
GRACE	morning. Where did you find her?!
CROYDON	At Veronica Fox’s place. Any idea
CROYDON	what she would’ve been doing there?
GRACE	No idea. I’m always finding her in
GRACE	the weirdest places...
JONES	I don’t remember seeing a dog at
JONES	your place.
GRACE	She’s an inside dog... And she’s
GRACE	shy.
JONES	You should put an address or number
JONES	on her collar, yeah?
JONES	She sure is happy to see you!
GRACE	Thanks for finding her. I’ll fix
GRACE	her collar, I promise.
GRACE	Everything okay at Veronica Fox’s
GRACE	place?
JONES	Why do you ask?
CROYDON	Do we have a budding cop on our
CROYDON	hands?
GRACE	Well... isn’t the case closed?
CROYDON	We don’t really use that term,
CROYDON	but... yeah.
GRACE	Cool.
CROYDON	Alright then. Get that collar
CROYDON	fixed, okay?
GRACE	Let’s get you back to your mama,
GRACE	huh? She must be beside herself.
GRACE	Come! Good girl! Come on!
GRACE	Claudia? It’s me.
CLAUDIA	Thank you.
CLAUDIA	Please don’t leave again.
GRACE	I won’t.
GRACE	I’m going to make you breakfast.
GRACE	Coffee?
CLAUDIA	I’ve never tried it...
GRACE	Me neither, but I’ve always wanted
GRACE	to drink black coffee in the
GRACE	morning.
GRACE	I want to be the lady who reads the
GRACE	papers in the garden as she sips on
GRACE	coffee. Looking out at the sunny
GRACE	day ahead with a sigh of
GRACE	satisfaction.
CLAUDIA	I can see it - you’d be wearing a
CLAUDIA	long dress and lots of jewels.
CLAUDIA	That is disgusting!
GRACE	Oh my God.
GRACE	We need sugar! All of it!
GRACE	I couldn’t find sugar but these are
GRACE	basically like sugar cubes.
CLAUDIA	What are they?
GRACE	Marshmallows.
GRACE	How many do you think I can fit
GRACE	into my mouth?
CLAUDIA	What?
GRACE	How many... do you think... I can
GRACE	fit... in my mouth?
CLAUDIA	Stop! You’re going to choke!
GRACE	Help! Take some out!
CLAUDIA	Wow.
CLAUDIA	It’s so sweet!
GRACE	So I was thinking... maybe we could
GRACE	decorate your room a bit today.
CLAUDIA	Why?
GRACE	I just thought it’d be nice to have
GRACE	some colour.
CLAUDIA	I don’t know... it feels weird
CLAUDIA	changing our room so soon.
GRACE	Our room?
CLAUDIA	Yeah... mine and mum’s.
GRACE	You shared a room with your mum?
CLAUDIA	Yeah.
CLAUDIA	I wouldn’t know how to do it.
GRACE	Do what?
CLAUDIA	Decorate.
GRACE	Lucky you have me.
GRACE	Let’s start with the walls.
CLAUDIA	Are we going to paint them?
GRACE	Better.
CLAUDIA	Do you know these people?
GRACE	I wish!
CLAUDIA	What do we do with them?
GRACE	We stick them on the wall. These
GRACE	are your new guardian angels.
GRACE	The trick to collaging is you can’t
GRACE	overthink it. Just start putting
GRACE	them up anywhere, like this.
CLAUDIA	I love it.
GRACE	Okay, now the bed.
CLAUDIA	What are you doing?
GRACE	You’ll see. Take the covers off
GRACE	yours.
CLAUDIA	How many do we need?
GRACE	I don’t know. I guess it depends
GRACE	how dark we want the dye to be.
CLAUDIA	Not too dark.
GRACE	I hope it turns out to be purple,
GRACE	not blue.
CLAUDIA	Same.
GRACE	Whatever colour it is, it’ll be
GRACE	better than white.
GRACE	It’s like a cubby house! Come in
GRACE	here!
GRACE	Ouch!
CLAUDIA	Are you okay?
GRACE	Yeah... prickle.
CLAUDIA	Let me see.
CLAUDIA	Better?
CLAUDIA	Better?
CLAUDIA	Better?
GRACE	Ready? Hold my hand.
CLAUDIA	It feels so weird!
CLAUDIA )	Tilly!
CLAUDIA	Where did you get all this stuff?
GRACE	Around. Most of it I’ve had for
GRACE	ages. Some of it I got from the
GRACE	city.
CLAUDIA	You’ve been to the city?
CLAUDIA	What’s it like?
GRACE	Busy, smelly... I love it.
CLAUDIA	Are you eating your necklace?
GRACE	Try it.
CLAUDIA	So yummy!
GRACE	I’ve also got bracelets, I think...
CLAUDIA	What’s that?
CLAUDIA	Wow!
GRACE	Close your eyes.
CLAUDIA	Can I choose the other colour?
GRACE	You don’t want them to match?
CLAUDIA	Oh... do they have to match?
GRACE	No, sorry, I don’t know why I said
GRACE	that. What colour?
GRACE	Nice.
CLAUDIA	Can I do you?
CLAUDIA	Can I choose your colours?
GRACE	Sure!
CLAUDIA	Close.
CLAUDIA	Okay, you choose the other colour.
GRACE	We should take a picture!
GRACE	Come over to the window!
CLAUDIA	What are you doing?
GRACE	Smile!
CLAUDIA	Why did you do that?
GRACE	All will be revealed in about five
GRACE	minutes, trust me!
CLAUDIA	Are they paint?
GRACE	Kinda. Paint for your lips.
CLAUDIA	Aren’t we supposed to be decorating
CLAUDIA	the room not ourselves?
GRACE	These are decorations! You can line
GRACE	them up on your dresser. Plus, they
GRACE	smell really good.
GRACE	Try to guess the flavour.
GRACE	Come on... guess.
CLAUDIA	Apple?
GRACE	Beginner’s luck.
CLAUDIA	Hmm... watermelon?
GRACE	Wow, I think I’ve met my match.
GRACE	Okay, bet you can’t get this one.
GRACE	This one is limited edition.
GRACE	Give up?
CLAUDIA	No!
GRACE	Want a hint?
CLAUDIA	I’ve never tasted it before.
GRACE	It’s Coca-cola.
GRACE	Want to try another?
CLAUDIA	Strawberry.
GRACE	You’re very good at this.
CLAUDIA	I like this flavour; it reminds me
CLAUDIA	of strawberry milk.
CLAUDIA	Ready?
GRACE	Ready!
CLAUDIA	Okay, my turn!
GRACE	Ready?
CLAUDIA	Yes!
GRACE	It’s going to be cold...
CLAUDIA	Do it!
CLAUDIA	Are you afraid that someone’s going
CLAUDIA	to come looking for you?
CLAUDIA	How come?
GRACE	Because no one cares enough to do
GRACE	that with me.
CLAUDIA	Not even if you’re out late?
GRACE	Probably not.
CLAUDIA	Not even if you’re out overnight?
GRACE	Why do you ask?
GRACE	It’s weird going home.
GRACE	Going from here to there is like
GRACE	riding my bike from heaven to hell.
CLAUDIA	Maybe you could spend one night in
CLAUDIA	heaven?
GRACE	Do you like it?
CLAUDIA	I love it.
GRACE	I think I really like you.
CLAUDIA	I think I really like you too.
CLAUDIA	You taste really sweet.
CLAUDIA	I don’t know what to do.
GRACE	Me neither.
CLAUDIA	Maybe we could start by breathing
CLAUDIA	together?
CLAUDIA	Deep breath in...
CLAUDIA	And out...
CLAUDIA	In...
CLAUDIA	And out...
CLAUDIA	In...
CLAUDIA	And...
GRACE	It’s really hard to do both at the
GRACE	same time!
CLAUDIA	Tilly!
CLAUDIA	I am so sorry; that was really
CLAUDIA	embarrassing.
GRACE	What?
GRACE	Come back! Don’t look at me from
GRACE	over there!
CLAUDIA	You are so beautiful.
CLAUDIA	Grace?
DONNA	What’s this about a fucking dog?
GRACE	I’ve been dog sitting a friend’s-
DONNA	Don’t you lie to me! I know you
DONNA	don’t have any friends.
GRACE	Thanks Mum. No need to be a bitch
GRACE	about it.
CROYDON	Let’s just calm down.
JONES	Grace, if you could pull up a seat.
JONES	We’ve got a couple of questions for
JONES	you.
JONES	Grace, if you could...
GRACE	“Beautiful Claudia, now is the time
GRACE	to explore who you really are.
GRACE	Play, experiment, be colourful and
GRACE	messy and free. I’ll be right here
GRACE	by your side, I purple promise.
GRACE	Love, G.”
GRACE	Please don’t!
CROYDON	She’s sixteen, Grace.
GRACE	So what?!
CROYDON	It’s the law. All minors without a
CROYDON	suitable parental guardian have to
CROYDON	be taken under care of the state
CROYDON	until they reach seventeen.
GRACE	I’m looking after her! I’m ten
GRACE	times better than any adult in this
GRACE	shit hole town!
JONES	It’s only for a year or so. And the
JONES	care homes can be pretty good.
GRACE	There has to be another way! She
GRACE	could live here with me!
CROYDON	It’s for her own good, Grace. You
CROYDON	can’t see that now, but it is.
GRACE	That’s fucking bullshit!
DONNA	Get back here right now!
GRACE	Please! Let me see her first at
GRACE	least?! You’ll scare her!
GRACE	You know nothing about her! She’s
GRACE	only ever seen her mum and me.
GRACE	You’ll spook her!
CLAUDIA	You miss her too, don’t you?
CLAUDIA )	She’s here! Come on! Come!
GRACE	Claudia!
GRACE )	No, no, no!
GRACE )	Let me out!
CROYDON	Tell us where she’s going, and-
GRACE	She’s terrified, okay? I know where
GRACE	she’s going. I’ll get her.
CLAUDIA	My mother said to hold on tight and
CLAUDIA	not let go. No matter what, never
CLAUDIA	let go.
VERONICA	This is a good one.
VERONICA	Deep breaths, okay, baby?
VERONICA	In...
VERONICA	And out...
VERONICA	Are we ready?
VERONICA	You’re safe now, sweetheart. A few
VERONICA	more steps.
GRACE	CLAUDIA!
VERONICA	Look at me. Focus on me. I know
VERONICA	it’s scary but soon it will all be
VERONICA	over and we’ll be together.
GRACE	CLAUDIA!
GRACE	Help me, Claudia, please!
GRACE	Let me help you!
CLAUDIA	Let go of me!
GRACE	Claudia, please-
CLAUDIA	I trusted you!
GRACE	Let me explain-
CLAUDIA	They’re going to take me!
CLAUDIA	Why do you want them to take me?
GRACE	That’s the last thing I want,
GRACE	Claudia, you have to believe me.
CLAUDIA	What do I do?
GRACE	I don’t know.
CLAUDIA	What do we do?!
GRACE	We’re going to be okay. Even if you
GRACE	have to go away for a little bit...
GRACE	We’re going to be okay.
CLAUDIA	Do you purple promise?
GRACE	I Purple promise.
GRACE	In...
CLAUDIA	And out.
"""

with open(file_path, 'w', encoding=encoding) as file:
    file.write(example_text)

# Run the function
find_consecutive_repeated_dialogs(file_path, encoding)