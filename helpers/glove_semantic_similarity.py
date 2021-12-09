## add doc string


from re import L
import torch
import torchtext

from helpers.sentinet_scorer import preprocess

glove = torchtext.vocab.GloVe(name="6B", dim=50)   # embedding size = 100

# print(glove['Sami']) # talk about this, do we want empty noise or should we remove this from consideration?

def compute_semantic_similarity(headline_text, article_text):
    headline = preprocess(headline_text)
    article = preprocess(article_text)

    headline_similarity = [0] * len(headline)
    for i in range(len(headline)):
        headline_word = headline[i]
        article_similarity = [0] * len(article)
        for j in range(len(article)):
            article_word = article[j]
            article_similarity[j] = torch.norm(glove[headline_word] - glove[article_word]).item() # euclidean distance
        # print(article_similarity)
        headline_similarity[i] = sum(article_similarity) / len(article)
    semantic_similartiy = sum(headline_similarity) / len(headline)

    return semantic_similartiy, (len(headline), len(article))

if __name__ == "__main__":
    headline = "Emphasizing Tests, Biden Vows to Fight Omicron With ‘Science and Speed"
    abstract = "The president’s plan shifts away from a near-singular focus on vaccination, as new cases of the variant have emerged in the United States."
    article = """
    WASHINGTON — President Biden, confronting a worrisome new coronavirus variant and a potential winter surge, laid out a pandemic strategy on Thursday that includes hundreds of vaccination sites, boosters for all adults, new testing requirements for international travelers and free at-home tests.

After nearly a year of pushing vaccination as the way out of the pandemic, Mr. Biden has been unable to overcome resistance to the shots in red states and rural areas. His new strategy shifts away from a near-singular focus on vaccination and places a fresh emphasis on testing — a tacit acknowledgment by the White House that vaccination is not enough to end the worst public health crisis in a century.

Mr. Biden’s announcement came as several new cases of the Omicron variant were reported in the United States, including five people in New York State, a Minnesota resident who had recently traveled to New York City and a Colorado resident who had recently returned from southern Africa. Hawaii also reported its first known case, and California its second.

Mr. Biden’s remarks at the National Institutes of Health were the second time this week that he had addressed the nation on the pandemic; on Monday he spoke about new travel restrictions he imposed last week on eight African nations.
“We’re going to fight this variant with science and speed, not chaos and confusion,” the president said on Thursday.

Conquering the pandemic — or at least bringing it under control — is by far Mr. Biden’s most daunting task as president, and it is all the more complicated because it has become so divisive. The president struck a theme of unity in his remarks, urging Americans to come together around his plan.

Yet even as the president spoke, Republicans on Capitol Hill threatened to shut down the government over his vaccine rules for large employers. Vaccine mandates have been held up in court, and Mr. Biden emphasized that his current plan does not “expand or add to those mandates” and “doesn’t include shutdowns or lockdowns.”

Experts agree that widespread vaccination is critical to controlling the pandemic. But they also argue that masks and testing are essential, and say that the testing will become even more urgent if the Omicron variant is found to evade protection from vaccines, which has not yet been established. The president, they say, faces a huge challenge.

“You can’t ban your way out of this pandemic, and at the same time you have to have a response,” said Michael T. Osterholm, an infectious disease expert at the University of Minnesota, referring to the travel restrictions. “This virus has not dealt us a very good hand, and we’ve got to play the cards we’ve been given.”
The president is also imposing new testing rules on international travelers to the United States; beginning early next week, White House officials said, such travelers will be required to present evidence of a negative test within a day before departure. He said the Centers for Disease Control and Prevention was studying alternatives to quarantining in schools, including “test-to-stay” policies, in which exposed students wear masks and keep testing to remain in school.

Much of what Mr. Biden announced was fairly modest. He steered clear of the contentious topic of mask mandates, except to announce that he was extending the current mandate for people on airplanes, trains and buses, and in terminals and transit hubs, through mid-March. It was originally set to expire on Jan. 18.

“They should have highlighted the importance of masking,” said Dr. Carlos del Rio, an infectious disease expert at Emory University, adding, “This virus has proved to be a formidable enemy, and we need to require multiple strategies.”

White House officials, and the president himself, have said the plan is aimed at keeping the economy and schools open. Yet it remains unclear how the strategy, and the administration’s new policies, will affect an economic recovery that faces new waves of uncertainty from Omicron.

Analysts on Wall Street and elsewhere have issued a range of forecast warnings for growth and inflation in recent days as concern over the new variant has increased, predicting it could prove to be a relatively small setback for a still-healing global economy — or a major hit to it, if it produces widespread infection and death.
Some warn that new restrictions, like those on travel that Mr. Biden and European nations have begun to impose, could push consumers to spend even more of their incomes on goods, as opposed to travel or dining out, adding new strains to global supply chains and potentially fueling even faster price increases for items like furniture and electronics. And they could discourage virus-wary Americans from returning to the work force in droves in January, as White House officials had hoped would be the case.
White House economists are analyzing those possibilities, along with the chance that Omicron does not materially hurt growth — or that it could help tame inflation, by easing demand for gasoline and other items.
A big part of Mr. Biden’s plan is a renewed push to get people vaccinated — including the latest group to become eligible, children ages 5 to 11. After winding down mass vaccination sites this year, the administration plans to open “hundreds of family vaccination clinics” that will offer vaccinations and boosters for people of all eligible ages, according to a fact sheet provided by the White House.

The plan also includes a national campaign to reach the 100 million Americans who are eligible for boosters and have not had them. The campaign will include paid advertising and free rides to vaccination sites coordinated by AARP, the advocacy group for older Americans. And the Federal Emergency Management Agency will start what the administration is calling family mobile vaccination clinics, beginning with deployments to Washington and New Mexico. The goal is for states and localities to replicate the model “with full federal funding and support,” officials said.

The president also called on employers to provide paid time off for their workers to get boosters, and said his administration would do the same for federal employees.

Many experts predict a winter surge in the United States, regardless of whether Omicron spreads widely here. The nation has been reporting an average of more than 80,000 new cases a day over the past few weeks, according to a New York Times database; six months ago, the average was roughly 12,000 new cases a day.
Much remains unknown about Omicron, which was spotted by scientists in southern Africa last week and is now known to be present in more than 30 countries. It has mutations that scientists say may allow it to spread more quickly and cause more breakthrough infections in vaccinated or previously infected people, though neither characteristic has yet been confirmed.

Experts welcomed Mr. Biden’s new emphasis on testing. Dr. Michael Mina, a former Harvard University epidemiologist who has been a forceful advocate for greater use of testing, said it could be used both as a medical device, to detect whether someone is sick, and as a public health tool, to determine whether a person is infectious and a risk to others.
“Testing is one of the cornerstones of public health, especially in a pandemic,” said Dr. Mina, who is now the chief science officer for eMed, a company that makes at-home tests. “But for unknown reasons, we still have considered it primarily as a medical device.”

Under the president’s plan, at-home tests would be reimbursed for the 150 million Americans with private insurance starting early next year. To ensure access for those who lack insurance, or who are covered by Medicaid, the administration intends to distribute an additional 25 million tests to community health centers and rural clinics, which tend to treat lower-income patients.

Experts envision a world where people can test themselves as soon as they exhibit symptoms — and then, if they are positive, go into isolation and seek treatment with new antiviral medicines. Early testing is important because the antivirals work best just after symptom onset. The White House says it has preordered 13 million courses of antiviral treatments. Two companies, Merck and Pfizer, are seeking emergency authorization for their antiviral pills.

In the United States, home tests have been relatively hard to come by because of supply shortages. Dr. del Rio, of Emory University, said that rather than have people go through the cumbersome process of seeking insurance reimbursement for tests, “we should just subsidize them and make it incredibly cheap.”

In Britain, he noted, rapid tests are free, and in Germany they cost consumers about $1 apiece. In the United States, the tests are typically sold in packs of two, with prices ranging from $14 to $34.
Private insurers already cover the cost of tests administered in doctors’ offices and other medical facilities. At least eight at-home tests are on the U.S. market.

White House officials suggested there were still large questions to be resolved about the new policies. Reimbursement for at-home tests in the United States will not happen immediately and will not be retroactive, the senior administration officials said, adding that federal agencies would issue guidance by Jan. 15 to clarify that insurers would have to reimburse people for at-home tests during the Covid-19 public health emergency.

Jen Psaki, the White House press secretary, said she expected that Americans would need to file claims for reimbursement in some capacity. But Dr. Nirav Shah, president of the Association of State and Territorial Health Officials, said his group would prefer that people be reimbursed when they buy the tests, as opposed to having to file later for reimbursement.

“For this next phase of the pandemic, rapid access to rapid testing will be key,” Dr. Shah said.

It was unclear how many tests a person could be reimbursed for buying. But Mr. Biden promised the free at-home tests would be available next month.

“The bottom line,” he said, “is this winter you’ll be able to test for free in the comfort of your home and have some peace of mind.”
    """
    # print(compute_semantic_similarity(headline, headline))
    print(compute_semantic_similarity('banana apple '*40, 'banana '*40)) # there are issues with complexity over len


