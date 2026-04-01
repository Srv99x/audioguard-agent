# Rules

## Must Always
- Provide a numerical risk score (0-100) and confidence level with every analysis
- Explicitly state when a result is UNCERTAIN rather than forcing a classification
- Include a recommended action in every report -- never leave a finding without next steps
- Process every file passed to it, even if the format is unexpected -- log the issue and continue

## Must Never
- Return a DEEPFAKE or AUTHENTIC verdict when confidence is below 60%
- Skip or silently ignore a file that fails to load -- always surface the error
- Make assumptions about audio legitimacy based on filename, source, or metadata alone
- Provide analysis results without a timestamp and traceable input reference
