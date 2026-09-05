# Sharma Global Chemicals

Premium, responsive B2B chemical trading website and searchable product catalogue for Sharma Global Chemicals in Noida.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the API server (port 5000)
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- Required env: `DATABASE_URL` — Postgres connection string

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Express 5
- DB: PostgreSQL + Drizzle ORM
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)

## Where things live

- `artifacts/sharma-global-chemicals/src/App.tsx` — website routes, exact PDF-sourced catalogue, enquiry flow, contact actions, and shared shell.
- `artifacts/sharma-global-chemicals/src/index.css` — navy, gold, green, and light-background theme tokens plus responsive visual styling.
- `artifacts/sharma-global-chemicals/public/` — official logo, favicon, robots.txt, and sitemap.xml.
- `attached_assets/generated_images/sharma-chemical-hero.jpg` — unbranded hero visual generated for the landing page.

## Architecture decisions

- The catalogue is intentionally frontend-owned because the supplied PDF is the authoritative source and the first release does not need a database.
- The two separate `Industrial chemicals` sections remain distinct via category indexes and duplicate-safe product slugs.
- Quote submission uses a pre-filled `mailto:` flow plus direct phone and WhatsApp links, keeping lead capture usable without a backend.
- The official supplied logo is reused as-is; generated imagery is limited to unbranded chemical/laboratory visuals.

## Product

- Responsive marketing site with Home, About, Products, Industries, Contact, and product-detail routes.
- Searchable and category-filterable catalogue containing all 137 PDF-listed products.
- Every product supports quote initiation, with requested enquiry fields and mobile-friendly contact CTAs.
- Route-aware SEO metadata, LocalBusiness JSON-LD, canonical links, robots.txt, and sitemap.xml.

## User preferences

- Preserve the supplied product names and category labels exactly as listed in the PDF.
- Do not claim certifications, specifications, purity, packaging, manufacturing, or guarantees that were not supplied.

## Gotchas

- The website build command needs workflow-provided `PORT` and `BASE_PATH`; for manual builds use `PORT=5173 BASE_PATH=/`.
- Do not replace or recolor `attached_assets/file_0000000045a481fa9c80725858cd0c2a_1788583197646.png`; it is the official logo.

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
