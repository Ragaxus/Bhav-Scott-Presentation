---
marp: true
theme: uncover 
title: Bhav And Scott Birthday Presentation 2026
transition: cube
paginate: true 
---
<style>
section.fibonacci {
	background-color: #F1DEDE;
	color: #363032;
	.number {
		color: #EEBC18;
	}
}
section.not-fibonacci {
	background-color: #363032;
	color: #507498;
}
.hebrew {
	font-family: bold;
}
</style>

<style scoped>
    h1,h2,h3 {
        font-family: "Courier New"
    }
</style>

<!-- paginate: false -->

# 2026-06-13 

<!-- transition: none-->

---

<style scoped>
    .number {
		color: #EEBC18;
    }
    * {
        text-align: center;
    }
    li {
        list-style-type: none;
    }
</style>

- <span class="number">8 </span> topics
* One minute each
* Let's go

<!-- transition: cube -->

---

<style scoped>
    section {
        display: block;
    }
</style>

<!-- class: fibonacci topic1a -->
<!-- paginate: true -->

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-1a.svg")
    }
</style>

# <span class="number">1.</span> A Hebrew lesson
### a. Common words and phrases <a name="hebrew-phrases"> </a>


<!-- transition: none -->

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-1a.svg")
    }
</style>

# <span class="number">1.</span> A Hebrew lesson
### a. Common words and phrases

<section>
<span class="hebrew">.תודה. בבקשה</span>

*(Todah. B'vahkeshah.)*

Thank you. You're welcome.
</section>

<!-- transition: none -->

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-1a.svg")
    }
</style>

# <span class="number">1.</span> A Hebrew lesson
### a. Common words and phrases

<section>
<span class="hebrew">.יריתי בציפור שלך כי היית איום</span>

*(yariti betzipur shelach ki hayeet ium)*

I bolted your bird because you are the threat.
</section>

<!-- transition: none -->

---


<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-1a.svg")
    }
</style>

# <span class="number">1.</span> A Hebrew lesson
### a. Common words and phrases

<span class="hebrew">.תֹּאכְלוּ זכוכית </span>

*(to'chlu zchuchit)*

Eat glass.

<!-- transition: fade -->
---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-1b.svg")
    }
</style>

# <span class="number">1.</span> A Hebrew lesson
### b. Shoreshim <a name="hebrew-shoreshim"> </a>

* "roots" 
   * "shoresh" means "root", "-im" is pluralization
* Means by which words are constructed in Hebrew and other Semitic languages

<!-- transition: none-->
---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-1b.svg")
    }
</style>

<style>
	.shoresh1 {
		color: red;
	}
	.shoresh2 {
		color: green;
	}
	.shoresh3 {
		color: blue;
	}
</style>

# <span class="number">1.</span> A Hebrew lesson
### b. Shoreshim

|Hebrew word|pronunciation|meaning|
|---|---|---|
|<span class="shoresh1">מֶ</span><span class="shoresh2">ל</span><span class="shoresh3">ךְ</span>| _(melekh)_ | king
|<span class="shoresh1">מ</span><span class="shoresh2">ַלְ</span><span class="shoresh3">כָּ</span>ה | *(malkah)* | queen
|<span class="shoresh1">מַ</span><span class="shoresh2">לְ</span ><span class="shoresh3">כ</span>וּת | _(malkut)_ | kingdom

<!-- transition: cube -->
---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-2.svg")
    }
</style>

# <span class="number">2. </span> The history of birthdays

<!-- transition: fade -->
---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-2.svg")
    }
</style>

<style>

/*==================================
    TIMELINE
==================================*/

    /*-- GENERAL STYLES
    ------------------------------*/
    .timeline {
        line-height: 1.4em;
        list-style: none;
        margin: 0;
        padding: 0;
        width: 100%;
        h1, h2, h3, h4, h5, h6 {
            line-height: inherit;
        }
    }

    /*----- TIMELINE ITEM -----*/

    .timeline-item {
        padding-left: 40px;
        position: relative;
		padding-bottom: 40px;
        &:last-child {
            padding-bottom: 0;
        }
    }

    /*----- TIMELINE INFO -----*/

    .timeline-info {
        font-size: 24px;
        font-weight: 600;
        letter-spacing: 3px;
        white-space: nowrap;
    }
    /*----- TIMELINE MARKER -----*/

    .timeline-marker {
        position: absolute;
        top: 0; bottom: 0; left: 0;
        width: 24px;
        &:before {
            background: #FF6B6B;
            border: 3px solid transparent;
            border-radius: 100%;
            content: "";
            display: block;
            height: 15px;
            position: absolute;
            top: 18px; left: 0;
            width: 15px;
            transition: background 0.3s ease-in-out,
                    border 0.3s ease-in-out;
        }
        &:after {
            content: "";
            width: 3px;
            background: #CCD5DB;
            display: block;
            position: absolute;
            top: 45px; bottom: -10px; left: 8.5px;
        }
        .timeline-item:last-child &:after {
            content: none;
        }
    }
    .timeline-item:not(.period):hover .timeline-marker:before {
        background: transparent;
        border: 3px solid #FF6B6B;
    }

    /*----- TIMELINE CONTENT -----*/

    .timeline-content {
        p:last-child {
            margin-bottom: 0;
        }
    }

    /*----- TIMELINE PERIOD -----*/
    
    .period {
        padding: 0;
        .timeline-info {
            display: none;
        }
        .timeline-marker {
            &:before {
                background: transparent;
                content: "";
                width: 15px;
                height: auto;
                border: none;
                border-radius: 0;
                top: 0;
                bottom: 30px;
                position: absolute;
                border-top: 3px solid #CCD5DB;
                border-bottom: 3px solid #CCD5DB;
            }
            &:after {
                content: "";
                height: 32px;
                top: auto;
            }
        }
        .timeline-content {
            padding: 40px 0 70px;
        }
        .timeline-title {
            margin: 0;
        }
    }

.timeline * {
	font-size: 22px;
	line-height: normal;
}

[data-bespoke-marp-fragment="inactive"] {
    opacity: 0;
    transition: opacity 0.5s ease;
  }

  [data-bespoke-marp-fragment="active"] {
    opacity: 1;
    transition: opacity 0.5s ease;
  }

</style>

## <span class="number"> 2. </span> The history of birthdays

<ul class="timeline">
	<li class="timeline-item">
		<div class="timeline-marker"></div>
        <div data-marpit-fragment="1">
            <div class="timeline-info">
                <span>Egypt, ~3000 BCE</span>
            </div>
            <div class="timeline-content" >
                <p>Celebrations for birthdays of royalty (important for astrological reasons)</p>
            </div>
        </li>
        <li class="timeline-item">
        </div>
		<div class="timeline-marker"></div>
        <div data-marpit-fragment="2">
            <div class="timeline-info">
                <span>Rome, 100s CE</span>
            </div>
            <div class="timeline-content" >
                <p>Birthdays for non-royalty (and candles on cakes)</p>
            </div>
        </div>
	</li>
	</li>
		<li class="timeline-item">
		<div class="timeline-marker"></div>
		<div data-marpit-fragment="3">
            <div class="timeline-info">
                <span>Europe, 1300s CE</span>
            </div>
			<div class="timeline-content">
                <p>Every infant was given the name of a saint as a protector. People celebrated their saint’s day, not their own birthday. </p>
            </div>
		</div>
	</li>
	</li>
		<li class="timeline-item">
		<div class="timeline-marker"></div>
		<div data-marpit-fragment="4">
		<div class="timeline-info">
			<span>Germany, 1700s CE</span>
		</div>
			<div class="timeline-content">
                <p> <i>Kinderfeste</i>, root of the modern birthday party </p>
                <p> This is when we start putting N candles on the cake </p> <!-- during an era when the individual person was seen as important and when childhood was “discovered” as a special stage of life (roots of modern birthday party) -->
            </div>
		</div>
	</li>
    <li class="timeline-item">
    <div class="timeline-marker">
    </div>
    <div data-marpit-fragment="5">
        <div class="timeline-info">
            Kentucky, 1893 CE
        </div>
        <div class="timeline-content">
            Patty and Mildred Hill compose <i>Happy Birthday To You</i>, which will become the most recognized song in English
        </div>
    </div>
    </li>
</ul>

<!-- transition: cube -->

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-3.svg")
    }
</style>


<style scoped>
	ul {
		list-style-type: none;
		text-align: center;
	}
</style>

<script>
  function playScale() {
    document.getElementById("cmix").play();
  }
</script>

# <span class="number">3.</span> The mixolydian scale

<audio id="cmix" src="./images/c-mix-mode-scale.mp3"> </audio>

<img src="./images/mixolydian-scale.png" width="500px" onclick="playScale()" />

- It's just a major scale, 
except that the 
seventh note is flat

<!-- transition: none -->

---
# <span class="number">3.</span> The mixolydian scale

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-3.svg")
    }
</style>

<video controls width=800 onclick="this.play()">

<source src="./images/sonic-3-hookpad.mp4"  type="video/mp4" />

</video>

<!-- transition: cube -->
---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-4.svg")
    }
</style>

<!--_class: not-fibonacci-->

# 4. Elephant grass

<!-- transition: fade -->
---


<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-4.svg")
    }
</style>

# 4. Elephant grass <a name="elephant-grass"> </a>
<!-- class: not-fibonacci -->
<!-- footer: "Illus. Tony Roberts. Map from tropicalforages.info"-->
<!-- Number four is elephant grass, a plant I learned about from the Magic: the Gathering card of the same name. It's native to sub-Saharan Africa, and it grows to a height of 4-7 meters, or 108 cheeseburgers on average. You can feed it to elephants, but you can also make paper with it, and you can also use it as part of a pest control method called push-pull. 

Maize is responsible for one-third of all the calories consumed in sub-Saharan Africa. It is parasited upon by an insect called the stemborer, which eats about ten percent of African maize crop yields annually. African farmers noticed that this insect is repelled by a plant called -->
<style>
	.two-cols {
		display: flex;
		flex-direction: row;
        height: 100%;
	}
	.two-cols div {
		padding-right: 10px
	}
    ul.grass-fact {
        height: 100%;
        li {
            display: grid;
            grid-template-columns: 30% 70%;
            font-size: 32px;
            list-style-type:none;
            justify-content: center;
            p {
                margin: auto 15px;
            }
        }
    }
</style>
 
<!-- <div>
    <img src="images/vis-104-elephant-grass.jpg" width="300" />
    <img src="images/Pennisetum_purpureum_F.jpg" width="300"/>
</div>
<div> 
</div>
<div>
</div> -->



<ul class="grass-fact">
<li data-marpit-fragment="1"> 

![w:300](images/Pennisetum_purpureum_F.jpg)
<p> Originates from sub-Saharan Africa </p>

<!-- 108 cheeseburgers -->

</li> 
<li data-marpit-fragment="2"> 

![w:300](images/vis-104-elephant-grass.jpg)
<p>Grows to a height of 4-7 meters </p>
</li>

</ul>


<!-- transition: none -->

---


<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-4.svg")
    }
</style>

# 4. Elephant grass
<!-- footer: ""-->

<style>
	.elephants-eat {
		font-size: 34px;
	}
    .col-info {
        width: 100%;
    }
    .col-info ul {
        text-align: center;
        list-style-type: none;
    }
    .two-cols {
        height: 100%;
    }
</style>

<p class="elephants-eat"> Things you can do with it </p>
<p class="elephants-eat"> other than let elephants eat it: </p>

<ul class="grass-fact">
<li>

![w:230](images/VibersBiopolymers-Jan-Govert-van-Gilst-800x566.jpg)
![w:230](images/elephant_grass_dried.jpg)

<p>Make paper</p>
</li>
</ul>

<!-- transition: none-->

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-4.svg")
    }
</style>

# 4. Elephant grass
<!-- footer: "One third of all sub-Saharan calories thing: [here](https://www.tandfonline.com/doi/full/10.1080/87559129.2019.1588290). More about push-pull with elephant grass and Desmodium: [here](https://www.fhcanada.org/blog/how-does-push-pull-pest-management-work)." -->

<!-- You plant the desmodium in rows alternating with the corn; the insects get repelled by the smell and jump into the elephant grass you've planted around the perimeter; they lay their eggs in it, and they don't hatch because the grass is hairy so they fall off

Checkmate bugs-->

<ul class="grass-fact">

<li data-marpit-fragment="1">

![w:230](images/stemborer.jpg)
<div>
<style scoped>
    li p {
        font-size: 24px;
    }
</style>
<p>Maize accounts for ~30% of all consumed calories in sub-Saharan Africa </p>
<p>Stemborers eat ~10% of it annually</p>
</div>
</li>
<li data-marpit-fragment="2"> 

![w:230](images/desmodium.jpg)

<p> Desmondium can be used in conjunction with elephant grass as <b>push-pull pest control</b> </p>
</li>

</ul>

<!-- transition: cube -->

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-5.svg")
    }
</style>

<!-- footer: "" -->
<!-- class: not-fibonacci -->
# 5. The golden ratio <a name="the-golden-ratio"></a>

<!-- Audio clip here of my saying "Stav I think you forgot to color this one gold"

Each fibonacci number in the talk will be gold

Golden rectangle but it's pictures of me and my family-->

<!-- transition: fade -->

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-5.svg")
    }
</style>

<!-- class: fibonacci -->
# <span class="number">5. </span> The golden ratio

<!-- transition: none -->

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-5.svg")
    }
</style>

# <span class="number">5. </span> The golden ratio
<section class="two-cols">
<div>

![w:300](images/Golden-ratio-line.svg.png)
</div>
<div>

Defined as the ratio of two lengths a/b, such that it is equal to the ratio of the larger length with their sum, a+b/a 
</div>
</section>

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-5.svg")
    }
</style>

<style>
	.formula {
		vertical-align: middle
	}
</style>

# <span class="number">5. </span> The golden ratio
<section class="two-cols">
<div>

![w:300](images/Golden-ratio-line.svg.png)

</div>
<p>

<img width=300 src="images/Golden-ratio-value.svg" class="formula"> 
1.618033988749...

</p>

</section>

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-5.svg")
    }
</style>

<style>
	.formula {
		vertical-align: middle
	}
</style>

# <span class="number">5. </span> The golden ratio
<section class="two-cols">
<div>

![w:300](images/Golden-ratio-line.svg.png)

</div>

![w:600](images/golden-ratio-derivation.png)

</section>

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-5.svg")
    }
</style>
# <span class="number">5. </span> The golden ratio

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 618" width="80%" height="80%">

<image x="0" y="0" width="618" height="618" class="rect-base r6" href="./images/golds/stav-georgia.jpg" preserveAspectRatio="xMidYMid slice" />
<image x="618" y="0" width="382" height="382" class="rect-base r5" href="./images/golds/maya-stella.jpg" preserveAspectRatio="xMidYMid slice" />
<image x="764" y="382" width="236" height="236" class="rect-base r4" href="./images/golds/mom.jpg" preserveAspectRatio="xMidYMid slice" />
<image x="618" y="472" width="146" height="146" class="rect-base r3" href="./images/golds/dad.jpg" preserveAspectRatio="xMidYMid slice" />
<image x="618" y="382" width="90" height="90" class="rect-base r2" href="./images/golds/maya.jpg" preserveAspectRatio="xMidYMid slice" />
<image x="708" y="382" width="56" height="90" class="rect-base r1" href="./images/golds/stav-little.jpg" preserveAspectRatio="xMidYMid slice" />
<path class="arc" d="        
M 708,472
    A 34,34 0 0,0 708,382
    A 90,90 0 0,0 618,472
    A 146,146 0 0,0 764,618
    A 236,236 0 0,0 1000,382
    A 382,382 0 0,0 618,0
    A 618,618 0 0,0 0,618
" />

<defs>
<style>
    /* 1. Set the initial states so they are ready but hidden */
    .rect-base {
        stroke-width: 1.5;
        opacity: 0; 
    }
    .arc {
        fill: none;
        stroke: #FFD700;
        stroke-width: 4;
        stroke-linecap: round;
        filter: drop-shadow(0px 0px 5px rgba(255, 215, 0, 0.6));
        stroke-dasharray: 2500;
        stroke-dashoffset: 2500;
    }
    .rect-base
    { 
        animation: fadeIn 0.6s ease-out forwards; 
    }
    .arc
    { 
        animation: drawSpiral 4s ease-in-out forwards;
    }
     .r1 { animation-delay: 0.1481s; }
     .r2 { animation-delay: 0.2963s; }
     .r3 { animation-delay: 0.5186s; }
     .r4 { animation-delay: 0.8888s; }
     .r5 { animation-delay: 1.4815s; }
     .r6 { animation-delay: 2.4444s; }
    @keyframes fadeIn { to { opacity: 1.0; } }
    @keyframes drawSpiral { to { stroke-dashoffset: 0; } }
</style>
</defs>
</svg>


---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-5.svg")
    }
</style>
# <span class="number">5. </span> The golden ratio

<div>

![](images/magic-dots-allied-enemy.webp)
</div>
</section>

<!-- transition: cube -->
---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-6.svg")
    }
</style>

<!-- class: not-fibonacci -->
# 6. Toilets <a name="toilets"> </a>
<!-- transition: fade -->
---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-6.svg")
    }
</style>
<!-- class: not-fibonacci -->
# 6. Toilets <a name="toilets"> </a>

<style>
    .not-fibonacci .timeline-marker:before {
        background: blue;
    }
	.caption p {
		font-style: italic;
		font-size: 14px;
	}
	.two-cols {
		gap: 20px;
	}
	.smaller-text * {
		font-size: 25px;
	}
    .continuer {
            content: "";
            width: 3px;
            background: #CCD5DB;
            display: block;
            position: absolute;
            top: 0; bottom: 540px; left: 78px;
    }
</style>

<ul class="timeline">
    <li class="timeline-item">
        <div class="timeline-marker"></div>
        <div data-marpit-fragment="1">
            <div class="timeline-info">
                <span>Indus River Valley, ~3000BC</span>
            </div>
            <div>
                <section class="two-cols">
                    <section id="baths">
<img src="./images/Great_bath_view_Mohenjodaro.webp" width="300">
<span class="caption"><p> The Great Bath at Mohenjo-Daro </p> </span>
                    </section>
                    <section class="smaller-text"> <p><i>"Several courtyard houses had both a washing platform and a dedicated toilet/waste disposal hole. The toilet holes would be flushed by emptying a jar of water, drawn from the house's central well, through a clay brick pipe, and into a shared brick drain, that would feed into an adjacent soak pit (cesspit)."</i></p>
                    </section>
                </section>
            </div>
        </div>
    </li>
<li> </li>
</ul>



<!-- footer: "thearchaeologist.org, \"Sanitation of the Indus Valley Civilisation\" "-->

<!-- transition: none -->

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-6.svg")
    }
</style>

<!-- footer: "sciencemuseum.org.uk, \"A flushing story\"" -->

# 6. Toilets

<div class="continuer"></div>
<ul class="timeline">
    <li class="timeline-item">
        <div class="timeline-marker"></div>
        <div data-marpit-fragment="1">
            <div class="timeline-info"> England, 1596 </div>
            <div class="timeline-content"> 
                <p>Sir John Harington, in his <i>The Metamorphosis of Ajax</i>, describes a flushing device</p>
            </div>
        </div>
    </li>
    <li class="timeline-item">
        <div class="timeline-marker"></div>
        <div data-marpit-fragment="2">
            <div class="timeline-info"> Scotland, 1775</div>
            <div class="timeline-content"> 
                <p>Alexander Cumming patents flushing toilet and provides the innovation of the S-pipe to seal odor away from the toilet bowl</p>
            </div>
        </div>
    </li>
    <li class="timeline-item">
        <div class="timeline-marker"></div>
        <div data-marpit-fragment="3">
            <div class="timeline-info">England, 1883</div>
            <div class="timeline-content">
<section class="two-cols"> 
<div>

![w:200](images/Model-of-the-Optimus-patent-water-closet-invented-by-Stevens-Hellyer-and-made-by-Dent-Hellyer-Limited-British-1870-1024x816.jpg)

</div>

<div>
<p>Twyford started using porcelain</p>
</div>
</section>
            </div>
        </div>
    </li>
    <li></li>
</ul>




---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-6.svg")
    }
</style>
# 6. Toilets
<!-- footer: "" -->
<style scoped>
	p.blurb { font-size: 24px; text-align: left}
    .continuer {
            content: "";
            width: 3px;
            background: #CCD5DB;
            display: block;
            position: absolute;
            top: 0; bottom: 505px; left: 78px;
    }
    .timeline-content li {
        font-size: 24px;
    }
</style>

<div class="continuer"></div>
<ul class="timeline">
    <li class="timeline-item">
        <div class="timeline-marker"> </div>
        <div data-marpit-fragment="1">
            <div class="timeline-info">Low Earth Orbit, 1983</div>
            <div class="timeline-content">
                <section class="two-cols">
                    <div> 
                        <img src="images/space-toilet.jpg" width="500px" />
                    </div>
                    <div>
                        <ul>
                            <li>Space Shuttle makes first flight with Waste Containment System (WCS): the first space toilet </li>
                            <li>Works by using a vacuum pump and airflow to direct waste into a water filtration system or a disposable bag</li>
                        </ul>
                    </div>
                </section>
</div>
</div>
</li>
<ul>

<!-- transition: cube -->
---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-7.svg")
    }
</style>

# 7. The art of Wylie Beckert <a name="wylie-beckert"></a>

<!-- transition: fade -->

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-7.svg")
    }
</style>

# 7. The art of Wylie Beckert <a name="wylie-beckert"></a>

<style>
	.quote p {
		font-size: 24px;
	}
    .gallery {
        margin: 0 150px 30px;
    }

	.wylie-gallery {
		display: flex;
		flex-direction: row;
		justify-content: space-evenly;
        
	}
</style>

<div class="wylie-gallery">

![](images/WylieBeckert-piranesi1000.jpg)![](images/WylieBeckert-carrier-600.jpg)![](images/WylieBeckert-takingtree-1000.jpg)

</div>

<div class="quote gallery">

*"The simultaneously grim and playful images she creates are distinguished by their intricate detail, unexpected compositions, and narrative sensibility, offering a window into a fantastical world that is both sinister and inviting."*
</div>

<!-- transition: fade -->

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-7.svg")
    }
</style>

# 7. The art of Wylie Beckert <a name="wylie-beckert"></a>

<style>
	.quote p {
		font-size: 24px;
	}
    .gallery {
        margin: 0 150px 30px;
    }

	.wylie-gallery {
		display: flex;
		flex-direction: row;
		justify-content: space-evenly;
        
        & img {
            height: 350px;
        }
	}
</style>

<div class="wylie-gallery">

![](./images/WylieBeckert-memorylapse.jpg)

</div>

<!-- transition: fade -->

---


<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-7.svg")
    }
</style>
<!-- footer: "Wylie Beckert, <i>Creating a Targeted Illustration Sample</i>, MuddyColors.com" -->

<style>
	.comparison {
		display: flex;
		gap: 40px;
	}
</style>

## 7. The art of Wylie Beckert

<div class="comparison">

<div class="quote">

*"To get hired by a specific client, it isn’t enough that work be “good” – it also has to be suited to the needs of the client...let’s say I want to get hired by [Wizards of the Coast]. The first thing I need to do is compare the work I’m doing to the work this client is hiring. Actually placing one of my own paintings among a few MTG pieces is rather eye-opening..."*
</div>

<div>

![h:300](images/wylie-mtg-comparison.jpeg)
![h:200](images/wylie-mtg-comparison-table.jpeg)
</div>



</div>

<!-- transition: cube -->

---

<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-8.svg")
    }
</style>

<!-- _class: fibonacci -->
<!-- footer: ""-->

# <span class="number">8.</span> Zeugma
<!-- transition: none -->
---
<!-- _class: fibonacci -->
<!-- paginate: false -->
<style scoped>
    p {
        font-size: 96px;
        font-family: "Comic Sans MS", "Comic Sans", cursive;
        transform: rotate(20deg);
        position: absolute;
        left: 400px;
    }
</style>

<p> zeugma nutz lol </p>

<!-- transition: fade -->
---


<style scoped>
    section::after {
        font-size: 0%;
        background-image: url("./images/progress-icons/progress-icon-8.svg")
    }
</style>
<!-- footer: "" -->
<!-- class: fibonacci -->
# <span class="number"> 8. </span> <a name="zeugma"> </a> Zeugma

<style>
	.container {
		display: flex;
		flex-direction: row;
		justify-content: space-evenly;
	}
	.definition {
		text-align: center;
		font-size: 24px;
		padding-bottom: 20px;
	}
	blockquote p {
		font-size: 32px;
	}
	.attribution {
		display: block;
		font-size: 24px;
	}
	.attribution::before {
		content: "—";
	}
</style>

<div class="definition">
	The use of a word to modify or govern two or more words, usually in such a manner that it applies to each word in a different sense.
</div>

<div>
<div class="container">

<div data-marpit-fragment="1">

>  You are free to execute your laws, and your citizens, as you see fit.
<p class="attribution"> Commander Riker</p>
</div>

<div data-marpit-fragment="2">

> Yet time and her aunt moved slowly — and her patience and her ideas were nearly worn out before the tete-a-tete was over.
<p class="attribution"> Jane Austen </p>

</div>

</div>
</div>

<!-- The notion that this is a cute way to inject wit into a sentence is the conclusion of this topic, as well as this presentation. -->

<!-- transition: fade -->

---
<!-- class: the-end -->
<style>
	td, th {
		text-align: left;
	}
	span.fib a,
	span.fib-number {
		color: gold;
	}
</style>

<a name="toc"></a>

| | |
|----|----|
<span class="fib-number"> 1a| [Hebrew: phrases](#hebrew-phrases)
<span class="fib-number">1b| [Hebrew: שורשים *(shoreshim)*](#hebrew-shoreshim)
<span class="fib-number">2| [History of birthdays](#birthdays)
<span class="fib-number">3| [The mixolydian scale](#mixolydian)
4| [Elephant grass](#elephant-grass)
<span class="fib-number">5| <span class="fib">[The golden ratio](#the-golden-ratio)</span>
6| [History of toilets](#toilets)
7| [The art of Wylie Beckert](#wylie-beckert)
<span class="fib-number">8| [Zeugma](#zeugma)

<!-- Fib sequence has two 1s, so that's why there's 1a and 1b -->
