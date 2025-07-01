# People Database Schema

## Person Record Structure

```yaml
person:
  # Basic Information
  name: "Full Name"
  slug: "filename-slug"
  photo_url: "https://example.com/photo.jpg"
  birth_year: 1985
  nationality: "Country"
  
  # Current Position
  current_role:
    title: "Job Title"
    organization: "Organization Name"
    location: "City, Country"
    start_date: "YYYY-MM"
    
  # Contact & Social
  links:
    website: "https://personal-site.com"
    twitter: "@username"
    linkedin: "https://linkedin.com/in/username"
    github: "username"
    scholar: "https://scholar.google.com/citations?user=ID"
    youtube: "https://youtube.com/channel/ID"
    
  # Professional
  expertise_areas:
    - "Primary Area 1"
    - "Primary Area 2"
    - "Secondary Area 1"
    
  # Recognition
  awards:
    - name: "Award Name"
      year: 2023
      description: "Brief description"
      
  # Research & Work
  notable_works:
    - title: "Paper/Book Title"
      year: 2023
      type: "paper|book|software|course"
      impact: "Brief impact description"
      
  # Relationships
  collaborators:
    - name: "Collaborator Name"
      relationship: "Co-author|Advisor|Student|Colleague"
      
  # Categorization
  categories:
    - "researcher"
    - "industry-leader"
    - "founder"
    - "educator"
    - "ai-safety"
    
  # Tracking
  last_updated: "YYYY-MM-DD"
  next_review: "YYYY-MM-DD"
  priority: "high|medium|low"
  status: "active|legacy|emerging"
```

## Category Definitions

### Primary Categories
- **researcher**: Academic or research-focused individuals
- **industry-leader**: C-level executives and senior leaders
- **founder**: Company founders and entrepreneurs
- **educator**: Teachers, course creators, and educational content creators
- **ai-safety**: Focused on AI safety, ethics, and alignment
- **investor**: VCs and investors in AI/ML space
- **communicator**: Journalists, podcasters, and science communicators
- **open-source**: Major open-source contributors

### Expertise Areas
- **Deep Learning**: Neural networks, architectures, training
- **Computer Vision**: Image processing, recognition, generation
- **Natural Language Processing**: Text processing, language models
- **Reinforcement Learning**: Decision making, game playing
- **Robotics**: Embodied AI, autonomous systems
- **AI Safety**: Alignment, robustness, interpretability
- **MLOps**: Production deployment, scaling, monitoring
- **Generative AI**: Content generation, creative AI
- **Multimodal AI**: Cross-modal learning and reasoning

### Impact Levels
- **Foundational**: Shaped the field's direction
- **Breakthrough**: Made significant discoveries
- **Scaling**: Brought AI to widespread adoption
- **Educational**: Taught thousands of practitioners
- **Ethical**: Advanced responsible AI development

## Maintenance Priorities

### High Priority (Monthly Updates)
- Recent news and achievements
- New publications or projects
- Role changes
- Link verification

### Medium Priority (Quarterly Updates)
- Photo updates
- Biography refinements
- Collaboration updates
- Award additions

### Low Priority (Annual Updates)
- Historical information
- Complete profile review
- Category reassessment
- Archive inactive profiles

## Data Sources

### Primary Sources
- Official websites and profiles
- Company announcements
- Academic publications
- Conference presentations
- Social media verified accounts

### Secondary Sources
- News articles and interviews
- Podcast appearances
- YouTube channels
- Wikipedia (with verification)
- Professional network profiles

### Verification Requirements
- Cross-reference multiple sources
- Use official or verified accounts
- Check recent activity for accuracy
- Update broken or outdated links
- Maintain photo attribution

## Automation Opportunities

### Link Monitoring
- Automated link checking
- Social media activity monitoring
- Publication tracking
- News mention alerts

### Content Generation
- Auto-generated recent updates
- Publication list maintenance
- Collaboration network mapping
- Impact metrics calculation

### Quality Assurance
- Template compliance checking
- Required field validation
- Duplicate detection
- Consistency verification

## Integration Points

### With Other Hubs
- **Concepts**: Link to related AI concepts
- **Books**: Connect to authored publications
- **Tools**: Link to created or associated tools
- **Companies**: Connect to founded or led organizations

### External Systems
- **Google Scholar**: Publication tracking
- **ORCID**: Research identification
- **LinkedIn**: Professional updates
- **Twitter**: Real-time updates
- **GitHub**: Code contributions

---

*This schema guides the systematic collection and maintenance of people data in the Digital Palace.*
