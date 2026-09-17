/**
 * Neo-Brutalist Design System
 * 
 * Palette:
 *   cream:    #E9ECEF
 *   card:     #FFFFFF
 *   ink:      #212529
 *   yellow:   #FB5607
 *   green:    #8338EC
 *   pink:     #8338EC
 *   blue:     #FB5607
 *   purple:   #8338EC
 *   orange:   #FB5607
 */

module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        extend: {
            colors: {
                cream:   '#E9ECEF',
                card:    '#FFFFFF',
                ink:     '#212529',
                yellow:  '#FB5607',
                green:   '#8338EC',
                pink:    '#8338EC',
                blue:    '#FB5607',
                purple:  '#8338EC',
                orange:  '#FB5607',
            },
            fontFamily: {
                sans: ['"DM Sans"', 'system-ui', 'sans-serif'],
                mono: ['"Space Mono"', 'Consolas', 'monospace'],
            },
            borderRadius: {
                'neo': '14px',
                'neo-sm': '10px',
                'neo-lg': '18px',
            },
            borderWidth: {
                'neo': '2.5px',
                '3': '3px',
            },
            boxShadow: {
                'neo':      '4px 4px 0px #212529',
                'neo-sm':   '2px 2px 0px #212529',
                'neo-lg':   '6px 6px 0px #212529',
                'neo-yellow': '4px 4px 0px #FB5607',
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
