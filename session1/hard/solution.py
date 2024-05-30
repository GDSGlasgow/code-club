import argparse

def flatten(lxs):
    return [l for lx in lxs for l in lx]

def find_the_key(messages: list, secrets: list):

    codedict = {}
    codelist = []
    output = []

    # flatten list of messages and strings (as the code should be the same for each)
    message_str = flatten(messages)
    secrets_str = flatten(secrets)

    # identify characters substituted in the secrets strings, and add them to a dictionary
    for i, j in enumerate(message_str):
        if j == secrets_str[i]:
            continue
        else:
            codedict[j] = secrets_str[i]

    # create the alpahabeticaly sorted character pairs and appendas list
    for k, v in codedict.items():
        codelist.append(sorted([k, v]))

    # flatten character pairs
    codelist = flatten(codelist)

    # create string pairs
    for i in range(0, (len(codelist)), 2):
        output.append(f'{codelist[i]}{codelist[i+1]}')

    # alpahabetically sort and remove duplicates
    output = sorted(list(set(output)))

    # create final string from list
    output = ''.join(output)

    return output


if __name__ == "__main__":
    CLI=argparse.ArgumentParser()
    CLI.add_argument(
      "--messages",
      nargs="*",
      type=str,
      default=["dance on the table", "hide my beers", "scouts rocks"],
    )
    CLI.add_argument(
      "--secrets",
      nargs="*",
      type=str,
      default=["egncd pn thd tgbud" ,"hked mr bddys" ,"scplts ypcis" ],
    )
    args = CLI.parse_args()
    messages = args.messages
    secrets = args.secrets
    print(find_the_key(messages, secrets))
