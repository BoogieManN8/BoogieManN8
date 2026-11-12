# Tengiz Kiknadze, Senior iOS Developer

Swift, SwiftUI, UIKit and Swift Concurrency. Based in Tbilisi, Georgia. Open to remote work and to relocation within Europe.

<a href="https://github.com/BoogieManN8"><img src="assets/btn-short-version.svg" height="36" alt="The short version: GitHub profile of Tengiz Kiknadze"></a>
<a href="https://www.linkedin.com/in/tengiz-kiknadze/"><img src="assets/btn-linkedin.svg" height="36" alt="Tengiz Kiknadze on LinkedIn"></a>
<a href="https://apps.apple.com/us/developer/tengiz-kiknadze/id1860013061"><img src="assets/btn-all-apps.svg" height="36" alt="All apps by Tengiz Kiknadze on the App Store"></a>

## About

I've been building iOS apps for 6 years. I started in 2020 as an intern at a cybersecurity group, writing MVVM modules for a live crypto trading app. Six months later I was leading the technical team. Nobody objected, so I kept going.

Since then I've built match-day dashboards that coaching staff at professional sports clubs used during games, a TikTok-style video feed for a social startup, and three apps of my own that I designed, built and took through App Store review solo. I've also led UIKit to SwiftUI migrations on production apps. Nobody misses the storyboards.

I care about two things more than most people find reasonable: architecture that still makes sense in its second year, and tests written before the code they cover. Neither is glamorous. Both are why I can refactor on a Friday.

## Now

Most of my hours currently go to backend, security and infrastructure on a live crypto exchange. It is the heaviest work I've done so far, and the details stay private. Real money has a way of sharpening your code review.

## Experience

### Technical Director (CTO), crypto exchange · Spring 2026 to present

- I run the technical side of a live exchange: backend, security, infrastructure and the team that ships it.

### Independent iOS Developer · Aug 2025 to present

- Designed, built and released three native iOS apps on my own: Miroa, Shelft and NovaThink. Architecture, UI, StoreKit 2 subscriptions, push notifications and App Store review were all mine to get wrong.
- Built Miroa test-first in VIPER with RIBs from the first commit. Regressions stayed rare and I could do large refactors in the middle of a release cycle.
- Set up CI/CD with GitHub Actions and Fastlane for build, test and TestFlight distribution.
- Put the Claude and Gemini APIs into production features. Most of that work was making structured output dependable enough to drive real UI.

### Senior iOS Engineer, consumer social app (early stage) · May 2025 to Aug 2025

- Built a TikTok-style vertical video feed from scratch with AVFoundation, a custom camera stack and native image filters, on a tight launch deadline.
- Agreed the API contracts with the backend team before feature work started. It saved both sides a lot of rework once traffic grew.

### Senior iOS Developer, sports technology platform · Aug 2023 to May 2025

The client is under NDA. The product is a real-time event management and performance analysis platform used by professional sports clubs.

- Built live match dashboards in SwiftUI and SpriteKit, fed over WebSockets, that coaching staff used during games. Latency budgets were tight, because a coach will not wait for a spinner.
- Shared ownership of the API contracts with the Android and backend teams (FastAPI, AWS), and brought a TensorFlow model's predictions into the iOS layer.
- Tightened security with in-house key encryption and fewer third-party dependencies.

### iOS Developer, freelance · Aug 2022 to Aug 2023

- Short contracts for small businesses: new features, bug fixes and App Store submissions on existing UIKit codebases.
- Used the flexible schedule to go deep on SwiftUI and Swift Concurrency. Both have been my daily stack in every role since.

### iOS Developer, then Head of Technical Team, cybersecurity group · Nov 2020 to Aug 2022

- Started hands-on with MVVM modules and WebSocket data pipelines for a cryptocurrency trading app with live market updates.
- Moved into the lead role within six months and went on to coordinate a 20-person team across backend, frontend and design, while staying close to the iOS code.
- Delivered four platforms under Scrum with ISO 27001 compliance. I later certified as an ISO 27001 Lead Implementer.

## Apps on the App Store

### Miroa

A private video and voice journal. You record, the app transcribes on the device, and nothing gets posted anywhere.

- On-device speech transcription, encrypted cloud backup to Cloudflare R2, AI analysis of entries
- Swift 6, SwiftUI, SwiftData, StoreKit 2
- VIPER with RIBs, written test-first from the first commit

<a href="https://apps.apple.com/us/app/miroa-private-video-journal/id6775486360"><img src="assets/btn-appstore.svg" height="30" alt="Miroa: Private Video Journal on the App Store"></a>

### Shelft

A warranty and receipt tracker. Photograph the receipt and the app reads the purchase details off it, then reminds you before the warranty runs out.

- Vision OCR pulls the purchase details out of the photo, on the device
- CloudKit sync across devices, so there is no backend to maintain
- Warranty expiry reminders

<a href="https://apps.apple.com/us/app/shelft-warranty-tracker-log/id6773617067"><img src="assets/btn-appstore.svg" height="30" alt="Shelft: Warranty Tracker and Log on the App Store"></a>

### NovaThink

An idea validation tool for founders. It is cheaper than building the wrong startup.

- LLM integration with structured output
- A dedicated iPad layout

<a href="https://apps.apple.com/us/app/novathink-new-startup-ideas/id6761935846"><img src="assets/btn-appstore.svg" height="30" alt="NovaThink: New Startup Ideas on the App Store"></a>

## How I work

| Pattern | Where I use it |
|:--|:--|
| VIPER with RIBs | My default for apps that will grow. Views stay dumb, presenters hold the state, interactors talk to managers. Every screen is built the same way, which makes a new one quick to add and boring to review. |
| MVVM and MVVM-C | Smaller apps, and older codebases where VIPER would be ceremony. |
| TCA (The Composable Architecture) | SwiftUI features with a lot of state, where I want one predictable data flow and reducers I can test. |
| Clean Architecture | Business logic that does not import SwiftUI or UIKit. That is what keeps it testable. |
| Networking | Typed endpoints on async/await and WebSocket connections that reconnect by themselves. I like the API contract agreed with backend before feature work starts. |

My own projects run Swift 6 with strict concurrency, and the rules are written down: no `DispatchQueue`, no `Task.detached`, no `@unchecked Sendable`, and no force unwrap without a documented reason. Writing rules down is cheaper than arguing about them in review.

## Open source

- [Networking](https://github.com/BoogieManN8/Networking): a small Swift networking layer on URLSession and async/await. It has typed endpoints, a WebSocket client that lives in an actor with reconnect and keep-alive, and zero dependencies.
- [CustomRouting](https://github.com/BoogieManN8/CustomRouting): a SwiftUI router that puts screens, alerts and modals behind one protocol.
- [SwiftUIStarterProject](https://github.com/BoogieManN8/SwiftUIStarterProject): my fork of the SwiftfulThinking starter for VIPER and RIBs in SwiftUI, with a script that scaffolds a new project.

Most of my commits sit in private repositories under NDA, so the contribution graph shows a fraction of the work.

## Stack

| Area | What I use |
|:--|:--|
| Languages and core | Swift, SwiftUI, UIKit, Swift Concurrency (async/await, actors), Combine, RxSwift, Objective-C interop |
| Architecture | VIPER, RIBs, TCA, MVVM, MVVM-C, Clean Architecture, SOLID, dependency injection, modularization with Swift Package Manager |
| Apple frameworks | AVFoundation, StoreKit 2, CloudKit, Core Data, SwiftData, WidgetKit, SpriteKit, Core ML, Vision, Speech, push notifications |
| Testing and tooling | XCTest, XCUITest, TDD, Instruments, Fastlane, GitHub Actions, TestFlight |
| Backend and integration | REST, WebSockets, JWT, Firebase, AWS, Cloudflare R2, LLM APIs (Claude, Gemini, OpenAI) |
| Practices | Code review, API contract design, accessibility, App Store release and compliance, mentoring, ISO 27001 |

I also write backend when a project needs one, mostly Python with FastAPI or Django. It means I can read the other side of the API contract, and lately I run that side too.

## Education and certifications

- B.Sc. Information Technologies, Business and Technology University, Tbilisi (expected 2026)
- ISO 27001 Lead Implementer
- SwiftUI Advanced Architecture

Languages: Georgian (native), English (full professional).

## Outside the day job

I build my own products because it keeps me honest. When you are the developer, the designer and the person answering App Store review, you stop gold plating fast.

## Contact

I'm open to senior iOS roles, remote or in Europe. Relocation is fine.

Email is the quickest way to reach me: [tengizkiknadze8@gmail.com](mailto:tengizkiknadze8@gmail.com)

<a href="mailto:tengizkiknadze8@gmail.com"><img src="assets/btn-email.svg" height="36" alt="Email Tengiz Kiknadze"></a>
<a href="https://www.linkedin.com/in/tengiz-kiknadze/"><img src="assets/btn-linkedin.svg" height="36" alt="Tengiz Kiknadze on LinkedIn"></a>
<a href="https://github.com/BoogieManN8"><img src="assets/btn-short-version.svg" height="36" alt="Back to the short version: GitHub profile of Tengiz Kiknadze"></a>
