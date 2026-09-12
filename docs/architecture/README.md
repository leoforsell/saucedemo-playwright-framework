# Architecture Documentation

The intended automation architecture is based on Playwright and JavaScript:

```mermaid
flowchart TD
    Tests[Tests and user intent] --> Fixtures[Custom fixtures]
    Fixtures --> Pages[Page Object Model]
    Pages --> Base[BasePage]
    Pages --> SauceDemo[SauceDemo application]
    Tests --> Assertions[Web-first assertions]
    Tests --> Network[Network interception]
    CI[GitHub Actions] --> Tests
    Tests --> Reports[HTML report, trace, screenshot, video]
```

The rendered architecture diagram will be added as `pom-architecture.png` during Week 14 after the implemented source structure is reviewed. The diagram must represent the actual code, not only the planned structure.
