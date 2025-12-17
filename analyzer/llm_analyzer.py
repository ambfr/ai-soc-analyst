from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_PATH = r"C:\Users\asgaj\models\gpt2"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model.eval()


def classify_ip(ip):
    if ip.startswith(("192.168.", "10.", "172.16.")):
        return "internal"
    return "external"


def safe_gpt_completion(prompt, max_tokens=25):
    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=0.4,
            top_k=30,
            repetition_penalty=1.2,
            no_repeat_ngram_size=3,
            pad_token_id=tokenizer.eos_token_id
        )

    text = tokenizer.decode(output[0], skip_special_tokens=True)
    completion = text[len(prompt):].strip()

    # Clean sentence
    sentence = completion.split(".")[0].strip()

    # Reject weak or vague completions
    bad_phrases = ["it has", "it can", "it allows", "probability", "used"]
    if len(sentence.split()) < 6 or any(p in sentence.lower() for p in bad_phrases):
        return "Such activity is commonly associated with patterns observed during security monitoring."

    return sentence.capitalize() + "."

def analyze_threat(suspicious_ips):
    results = {}

    for ip in suspicious_ips:
        ip_type = classify_ip(ip)

        if ip_type == "internal":
            origin = "Internal network"
            behavior = "Normal internal system activity"
            threat = "Low"
            action = "Continue monitoring"
            gpt_prompt = "This internal IP is considered low risk because"
        else:
            origin = "External network"
            behavior = "Suspicious access attempts"
            threat = "Medium"
            action = "Monitor and block if repeated"
            gpt_prompt = "This external IP is considered a security concern because"

        if ip_type == "internal":
             justification = "Internal traffic is considered low risk unless correlated with anomalous behavior."
        else:
            justification = safe_gpt_completion(gpt_prompt)

        report = (
            f"IP Address: {ip}\n"
            f"Origin: {origin}\n"
            f"Behavior: {behavior}\n"
            f"Threat Level: {threat}\n"
            f"Recommended Action: {action}\n"
            f"Justification: {justification}"
        )

        results[ip] = report

    return results
