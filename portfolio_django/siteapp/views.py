from django.shortcuts import render

COUNTS = [
    {
        "icon": "images/counter/star.svg",
        "value": "4.86",
        "description": "Out of 5 stars from 3896 reviews on Google platform",
    },
    {
        "icon": "images/counter/admin.svg",
        "value": "364",
        "description": "Client testimonials received in the year 2021",
    },
    {
        "icon": "images/counter/bag.svg",
        "value": "45M+",
        "description": "Revenue generated through new projects & marketing",
    },
]

PROGRESS_ITEMS = [
    {"title": "UX Research and Testing", "progress": 95, "width_class": "w-[95%]"},
    {"title": "Product Management", "progress": 84, "width_class": "w-[84%]"},
    {"title": "UI & Visual Design", "progress": 90, "width_class": "w-[90%]"},
]

SERVICE_ITEMS = [
    {
        "icon": "images/services/ux-design-product_1.svg",
        "title": "Full-Stack Product Engineering",
        "description": "From architecture to polished interfaces, I build production-ready products that are fast, secure, and maintainable.",
    },
    {
        "icon": "images/services/perfomance-optimization.svg",
        "title": "Performance and Scalability",
        "description": "I optimize systems for load, reliability, and cost efficiency so your platform can scale without painful rewrites.",
    },
    {
        "icon": "images/services/ux-design-product_2.svg",
        "title": "API and Backend Systems",
        "description": "I design robust APIs and backend services with clean data models, observability, and long-term engineering discipline.",
    },
]

PORTFOLIO_ITEMS = [
    {"image": "images/portfolio/cozycasa.png", "title": "Cozycasa Platform", "info": "Reduced onboarding friction and improved conversion flow."},
    {"image": "images/portfolio/mars.png", "title": "Mars Dashboard", "info": "Built role-based analytics with clean data pipelines."},
    {"image": "images/portfolio/humans.png", "title": "Everyday Humans", "info": "Delivered scalable content and membership architecture."},
    {"image": "images/portfolio/roket-squred.png", "title": "Rocket Squared", "info": "Re-engineered frontend performance for faster retention loops."},
    {"image": "images/portfolio/panda-logo.png", "title": "Panda Identity Suite", "info": "Shipped a unified digital brand and product interface."},
    {"image": "images/portfolio/cozycasa.png", "title": "InnovateX Ventures", "info": "Implemented secure API contracts for growth-stage operations."},
]

BLOG_ITEMS = [
    {
        "title": "How to Build Better Landing Pages",
        "date": "2025-04-10",
        "category": "Design",
        "image": "images/blog/blog_1.png",
        "excerpt": "A practical guide to improve conversion with cleaner layout and messaging.",
    },
    {
        "title": "Portfolio Tips That Win Clients",
        "date": "2025-05-21",
        "category": "Portfolio",
        "image": "images/blog/blog_2.jpg",
        "excerpt": "Structure, storytelling, and project framing that make your portfolio sell your work.",
    },
    {
        "title": "Scaling Frontend Performance",
        "date": "2025-07-02",
        "category": "Engineering",
        "image": "images/blog/blog_3.png",
        "excerpt": "Small performance improvements that create a faster user experience.",
    },
]


def _base_context():
    return {
        "counts": COUNTS,
        "progress_items": PROGRESS_ITEMS,
        "service_items": SERVICE_ITEMS,
        "portfolio_items": PORTFOLIO_ITEMS,
        "blog_items": BLOG_ITEMS,
    }


def home(request):
    return render(request, "siteapp/index.html", _base_context())


def about(request):
    return render(request, "siteapp/about.html", _base_context())


def services(request):
    return render(request, "siteapp/services.html", _base_context())


def portfolio(request):
    return render(request, "siteapp/portfolio.html", _base_context())


def blog(request):
    return render(request, "siteapp/blog.html", _base_context())


def contact(request):
    return render(request, "siteapp/contact.html", _base_context())
