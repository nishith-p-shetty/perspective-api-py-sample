from googleapiclient import discovery
import json
import os

API_KEY = 'YOUR_API_KEY'

client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey = API_KEY,
    discoveryServiceUrl = "https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery = False,
)

analyze_request = {
    'comment': { 'text': input("Enter Text : ") },
    'requestedAttributes': {
        'TOXICITY': {},
        'SEVERE_TOXICITY': {},
        'IDENTITY_ATTACK': {},
        'INSULT': {},
        'PROFANITY': {},
        'THREAT': {},
        'TOXICITY_EXPERIMENTAL': {},
        'SEVERE_TOXICITY_EXPERIMENTAL': {},
        'IDENTITY_ATTACK_EXPERIMENTAL': {},
        'INSULT_EXPERIMENTAL': {},
        'PROFANITY_EXPERIMENTAL': {},
        'THREAT_EXPERIMENTAL': {},
        'SEXUALLY_EXPLICIT': {},
        'FLIRTATION': {},
        'ATTACK_ON_AUTHOR': {},
        'ATTACK_ON_COMMENTER': {},
        'INCOHERENT': {},
        'INFLAMMATORY': {},
        'LIKELY_TO_REJECT': {},
        'OBSCENE': {},
        'SPAM': {},
        'UNSUBSTANTIAL': {},
        }
}

response = client.comments().analyze( body = analyze_request ).execute()

#print( json.dumps( response, indent = 3 ) )
#print( json.dumps( response["attributeScores"], indent = 3 ) )

params = ['TOXICITY', 'SEVERE_TOXICITY', 'IDENTITY_ATTACK', 'INSULT', 'PROFANITY', 'THREAT', 'TOXICITY_EXPERIMENTAL', 'SEVERE_TOXICITY_EXPERIMENTAL', 'IDENTITY_ATTACK_EXPERIMENTAL', 'INSULT_EXPERIMENTAL', 'PROFANITY_EXPERIMENTAL', 'THREAT_EXPERIMENTAL', 'SEXUALLY_EXPLICIT', 'FLIRTATION', 'ATTACK_ON_AUTHOR', 'ATTACK_ON_COMMENTER', 'INCOHERENT', 'INFLAMMATORY', 'LIKELY_TO_REJECT', 'OBSCENE', 'SPAM', 'UNSUBSTANTIAL']

parsed = json.dumps( response["attributeScores"])
parsed = json.loads(parsed)

for i in params:
    tmp = parsed[i]
    tmp = tmp['summaryScore']
    #print(i , " : " , tmp['value'])
    print( '{:28s} : {:4}'.format(i, tmp['value']) )