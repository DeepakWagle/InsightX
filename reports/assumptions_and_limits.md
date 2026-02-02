# Assumptions and Limitations

## Assumptions

- Psychometric attributes (O, C, E, A, N) are static personality traits collected
  through standardized employee assessments.
- All users in the psychometric dataset have complete personality scores, and
  no imputation is required for these attributes.
- Email activity is treated as a proxy for user behavior and communication
  patterns, not for intent or content interpretation.
- Users with limited or no email activity may represent roles that do not rely
  heavily on email communication rather than suspicious behavior.

## Limitations

- Behavioral analysis is limited to email metadata and does not capture actions
  performed outside email systems.
- Inactive users are identified solely based on email activity and may not
  reflect overall system usage.
- Email content is not semantically analyzed at this stage, limiting contextual
  interpretation of communication behavior.

## Decisions Taken

- No rows were removed due to missing psychometric data, as all users have
  complete personality scores.
- Email activity was evaluated to identify inactive users; however, no users
  met the inactivity criteria in this dataset.
- No temporal gap correction or interpolation was applied, as email activity
  shows strong temporal continuity.
