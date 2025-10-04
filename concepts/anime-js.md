# Anime.js

**Anime.js** is a lightweight JavaScript animation library with a simple, yet powerful API. It works with CSS properties, SVG, DOM attributes and JavaScript Objects, providing a complete animator's toolbox for web animations.

## Key Features

- **Intuitive API**: Easy-to-use yet powerful animation API with per-property parameters and flexible keyframes
- **Enhanced Transforms**: Smooth blending of individual CSS transform properties with versatile composition API
- **Scroll Observer**: Synchronize and trigger animations on scroll with multiple synchronization modes
- **Advanced Staggering**: Create stunning effects with built-in stagger utility for time, values, and timeline positions
- **SVG Toolset**: Morph shapes, follow motion paths, and draw lines with built-in SVG utilities
- **Springs and Draggable**: Drag, snap, flick and throw HTML elements with fully-featured Draggable API
- **Timeline Orchestration**: Powerful Timeline API for orchestrating animation sequences and keeping callbacks in sync
- **Responsive Animations**: Make animations respond to media queries with the Scope API
- **Lightweight & Modular**: Keep bundle size small by importing only needed parts

## Core Advantages

### **Performance & Compatibility**

- **Lightweight**: 24.50 KB bundle size
- **Cross-browser**: Works across modern browsers
- **Hardware Accelerated**: Leverages GPU acceleration for smooth animations
- **Modular**: Import only what you need to minimize bundle size

### **Developer Experience**

- **Simple API**: Intuitive syntax for complex animations
- **Flexible Keyframes**: Support for complex animation sequences
- **Built-in Easings**: Comprehensive set of easing functions
- **Function-based Values**: Dynamic values for responsive animations

## Implementation Patterns

### **Basic Animation**

```javascript
// Simple rotation animation
anime({
  targets: '.square',
  rotate: 90,
  loop: true,
  ease: 'inOutExpo',
});
```

### **Advanced Staggering**

```javascript
// Staggered animation with grid
const options = {
  grid: [13, 13],
  from: 'center',
};

anime.timeline()
  .add('.dot', {
    scale: anime.stagger([1.1, 0.75], options),
    ease: 'inOutQuad',
  }, anime.stagger(200, options));
```

### **SVG Morphing**

```javascript
// Morph one shape into another
anime({
  targets: '.circuit-a',
  d: [
    { value: 'M0,0 L100,0 L100,100 L0,100 Z' }, // Square
    { value: 'M50,0 L100,50 L50,100 L0,50 Z' }  // Diamond
  ],
  easing: 'easeInOutQuad',
  duration: 2000,
  loop: true
});
```

### **Motion Path**

```javascript
// Animate along a path
anime({
  targets: '.car',
  translateX: anime.path('.circuit')('x'),
  translateY: anime.path('.circuit')('y'),
  rotate: anime.path('.circuit')('angle'),
  easing: 'linear',
  duration: 2000,
  loop: true
});
```

### **Draggable Elements**

```javascript
// Create draggable element with spring physics
anime({
  targets: '.circle',
  translateX: anime.random(-100, 100),
  translateY: anime.random(-100, 100),
  scale: anime.stagger([1, 1.5], {grid: [5, 5], from: 'center'}),
  rotate: anime.random(-180, 180),
  duration: anime.random(500, 1000),
  easing: 'easeInOutQuad',
  complete: () => {
    // Animation complete callback
  }
});
```

### **Scroll-triggered Animation**

```javascript
// Trigger animation on scroll
anime({
  targets: '.element',
  translateY: [100, 0],
  opacity: [0, 1],
  easing: 'easeOutQuad',
  autoplay: false
}).playOnScroll({
  sync: true,
  threshold: 0.5
});
```

### **Responsive Animations**

```javascript
// Different animations based on media queries
const responsiveAnimation = anime.scope({
  mediaQueries: {
    portrait: '(orientation: portrait)',
    landscape: '(orientation: landscape)'
  }
});

responsiveAnimation.add(({ matches }) => {
  const isPortrait = matches.portrait;
  
  anime({
    targets: '.responsive-element',
    translateX: isPortrait ? [0, 100] : [0, 200],
    duration: 1000
  });
});
```

## Tools & Ecosystem

### **Official Resources**
- **[Anime.js Website](https://animejs.com/)** - Official documentation and examples
- **[GitHub Repository](https://github.com/juliangarnier/anime)** - Source code and issues
- **[CodePen Collection](https://codepen.io/collection/Poerqa)** - Interactive examples
- **[Easing Editor](https://animejs.com/easing-editor)** - Custom easing function editor

### **Community Tools**
- **Anime.js Plugins**: Community-developed extensions
- **Integration Libraries**: Wrappers for React, Vue, Angular
- **Build Tools**: Webpack, Vite, Rollup configurations

## Use Cases

### **Web Development**
- **Interactive Websites**: Engaging user interfaces with smooth animations
- **Loading Animations**: Professional loading states and transitions
- **Micro-interactions**: Subtle animations that enhance user experience
- **Data Visualization**: Animated charts and graphs

### **Creative Projects**
- **SVG Animations**: Complex shape morphing and path animations
- **Interactive Art**: Generative art and creative coding projects
- **Game Development**: UI animations and sprite animations
- **Prototyping**: Rapid animation prototyping for design systems

### **Production Applications**
- **Marketing Websites**: High-impact landing pages with animations
- **Web Applications**: Enhanced UX with smooth transitions
- **Mobile Web**: Touch-friendly draggable interfaces
- **Progressive Web Apps**: Offline-capable animated experiences

## Performance Optimization

### **Efficient Selectors**
```javascript
// Use efficient CSS selectors
anime({
  targets: document.querySelectorAll('.animated-element'),
  // ... animation properties
});

// Or use class names for better performance
anime({
  targets: '.animated-element',
  // ... animation properties
});
```

### **Timeline Optimization**
```javascript
// Group related animations in timelines
const timeline = anime.timeline({
  easing: 'easeOutExpo',
  duration: 750
});

timeline
  .add({
    targets: '.element-1',
    translateX: 250,
  })
  .add({
    targets: '.element-2',
    translateX: 250,
  }, '-=500'); // Start 500ms before previous animation ends
```

### **Memory Management**
```javascript
// Clean up animations when not needed
const animation = anime({
  targets: '.element',
  translateX: 100,
  autoplay: false
});

// Later, remove the animation
animation.remove();
```

## Integration Patterns

### **React Integration**
```jsx
import { useEffect, useRef } from 'react';
import anime from 'animejs';

function AnimatedComponent() {
  const elementRef = useRef(null);
  
  useEffect(() => {
    anime({
      targets: elementRef.current,
      translateX: [0, 100],
      duration: 1000,
      easing: 'easeInOutQuad'
    });
  }, []);
  
  return <div ref={elementRef}>Animated Element</div>;
}
```

### **Vue.js Integration**
```vue
<template>
  <div ref="animatedElement">Animated Element</div>
</template>

<script>
import anime from 'animejs';

export default {
  mounted() {
    anime({
      targets: this.$refs.animatedElement,
      translateY: [0, -50],
      duration: 800,
      easing: 'easeOutQuad'
    });
  }
}
</script>
```

### **Build Tool Integration**
```javascript
// webpack.config.js
module.exports = {
  // ... other config
  optimization: {
    splitChunks: {
      cacheGroups: {
        anime: {
          test: /[\\/]node_modules[\\/]animejs[\\/]/,
          name: 'anime',
          chunks: 'all'
        }
      }
    }
  }
};
```

## Related Concepts

- **[UI/UX Design Challenges](./ui-ux-challenges.md)** - Animation in user interface design
- **[Web Development Tools](../tools/development-tools/)** - Web development ecosystem
- **[Presentation Tools](./presentation-tools.md)** - Animation in presentations

## Best Practices

### **Animation Guidelines**
- **Purposeful Animations**: Every animation should serve a functional purpose
- **Performance First**: Use transform and opacity for best performance
- **Accessibility**: Respect user preferences for reduced motion
- **Consistent Timing**: Use consistent durations and easings across your site

### **Code Organization**
- **Modular Animations**: Break complex animations into reusable functions
- **Timeline Management**: Use timelines for complex sequences
- **Cleanup**: Remove unused animations to prevent memory leaks
- **Error Handling**: Handle cases where elements might not exist

### **Cross-browser Compatibility**
- **Fallbacks**: Provide fallbacks for older browsers
- **Feature Detection**: Check for animation support before animating
- **Progressive Enhancement**: Animations should enhance, not break, functionality

## Learning Resources

### **Official Documentation**
- **[Getting Started](https://animejs.com/documentation/getting-started)** - Basic setup and usage
- **[Animation Guide](https://animejs.com/documentation/animation)** - Complete animation API
- **[Timeline Documentation](https://animejs.com/documentation/timeline)** - Timeline orchestration
- **[SVG Guide](https://animejs.com/documentation/svg)** - SVG animation techniques

### **Community Resources**
- **[Anime.js Examples](https://codepen.io/collection/Poerqa)** - Interactive CodePen examples
- **[GitHub Discussions](https://github.com/juliangarnier/anime/discussions)** - Community support
- **[Tutorial Articles](https://animejs.com/learn)** - Learning materials
- **[Plugin Ecosystem](https://github.com/juliangarnier/anime/network/dependents)** - Community plugins

### **Integration Guides**
- **[React Anime](https://github.com/hyperfuse/react-anime)** - React wrapper library
- **[Vue Anime](https://github.com/BenAHammou/vue-anime)** - Vue.js integration
- **[Angular Animations](https://angular.io/guide/animations)** - Angular's animation system

## Future Directions

### **Emerging Features**
- **Web Animations API Integration**: Better WAAPI compatibility
- **CSS Houdini Support**: Advanced CSS custom properties animation
- **Machine Learning Integration**: AI-powered animation generation
- **WebGPU Acceleration**: Next-generation GPU acceleration

### **Community Growth**
- **Plugin Ecosystem**: More community-developed plugins
- **Framework Integrations**: Deeper integration with modern frameworks
- **Performance Improvements**: Smaller bundle sizes and better optimization
- **Educational Content**: More tutorials and learning resources

[Back to Concepts Hub](./README.md)